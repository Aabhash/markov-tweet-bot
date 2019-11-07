from markov_model import MarkovModel
from utility import Utility
import twitter
import time
from threading import Thread, Lock
import copy
import random
import pandas
import csv


class Tweeter:
    def __init__(self):
        """
        __init__  constructor of class Tweeter
        """
        self._autotweet_flag = False

        # Auto tweet attributes
        self._keywords = None
        self._prefix = None
        self._suffix = None

        self._interval = 1

        # API Access
        self._oauth = None
        self._t_auth = None
        self._ts_auth = None

        self._t_lock = Lock()
        self._ts_lock = Lock()

        # Login
        self._logged_in = False
        self._credentials = None

    def login(self, c_key, c_secret, a_token, a_t_secret):
        """
        login Logs into twitter using credentials provided

        :param c_key: client key for twitter
        :type c_key: str
        :param c_secret: client secret for twitter
        :type c_secret: str
        :param a_token: account token for twitter
        :type a_token: str
        :param a_t_secret: account token secret for twitter
        :type a_t_secret: str
        """

        self._oauth = twitter.OAuth(a_token, a_t_secret, c_key, c_secret)
        self._t_auth = twitter.Twitter(auth=self._oauth)
        self._ts_auth = twitter.TwitterStream(auth=self._oauth)
        self._logged_in = True

        self._credentials = self._t_auth.account.verify_credentials()

    def start_tweeting(self, time=0, jitter=0, keywords=None, prefix=None, suffix=None):
        """
        start_tweeting Starts auto tweeting


        :param time: interval of auto tweets, defaults to 0
        :type time: int, optional
        :param jitter: jitter size of tweets, defaults to 0
        :type jitter: int, optional
        :param keywords: keywords to be included in the tweets, defaults to None
        :type keywords: str, optional
        :param prefix: prefix to be included at the start of the text, defaults to None
        :type prefix: str, optional
        :param suffix: suffix to be included at the end of the text,, defaults to None
        :type suffix: str, optional
        """
        self._interval = time
        self._jitter = jitter
        self._keywords = keywords
        self._prefix = prefix
        self._suffix = suffix

        self._autotweet_flag = True

    def stop_tweeting(self):
        """
        stop_tweeting Stops auto tweeting 

        """
        self._interval = None
        self._jitter = None
        self._keywords = None
        self._prefix = None
        self._suffix = None

        self._autotweet_flag = False

    def __get_prefix_in_tweet(self):
        """
        __get_prefix_in_tweet Obtain prefix to include in tweet 


        :return: prefix to include in tweet
        :rtype: str
        """
        if self._prefix is None or type(self._prefix) in [str]:
            prefix = copy.deepcopy(self._prefix)
        elif type(self._prefix) in [list, tuple]:
            prefix = random.choice(self._prefix)
        else:
            prefix = None
            Utility.log('tweeter.get_prefix_in_tweet', 'Not using prefix')
        return prefix

    def __get_suffix_in_tweet(self):
        """
        __get_suffix_in_tweet Obtain suffix to include in tweet 


        :return: suffix to include in tweet 
        :rtype: str
        """
        if self._suffix == None or type(self._suffix) in [str]:
            suffix = copy.deepcopy(self._suffix)
        elif type(self._suffix) in [list, tuple]:
            suffix = random.choice(self._suffix)
        else:
            suffix = None
            Utility.log('tweeter.get_suffix_in_tweet', 'Not using suffix')
        return suffix

    def _autoconstruct(self, model, n_tweets=10):
        """
        _autoconstruct core tweeting logic 

        [extended_summary]
        automatically tweets new tweets automatically untill the number of tweets exhausts


        :param model: model to be included in this tweet session
        :type model: model
        :param n_tweets: number of tweets, defaults to 10
        :type n_tweets: int, optional
        """
        t_count = 0
        while self._autotweet_flag and t_count < n_tweets:
            # if self._logged_in and self._autotweet_flag:
            if self._autotweet_flag:
                if self._keywords is not None:
                    if type(self._keywords) in [str]:
                        keyword = self._keywords
                    else:
                        keyword = random.choice(self._keywords)
                if self._logged_in == False:
                    Utility.log('tweeter._autoconstruct', 'Not logged in')
                keyword = None

                prefix = self.__get_prefix_in_tweet()
                suffix = self.__get_suffix_in_tweet()

                new_tweet = self._construct_new_tweet(
                    model, seedword=keyword, prefix=prefix, suffix=suffix)

                self._t_lock.acquire(True)
                self.tweet(new_tweet)
                self._t_lock.release()

                Utility.log('tweeter.autotweet',
                            'Sleeping for {0} seconds'.format(self._interval))
                time.sleep(self._interval)
            t_count += 1

    def tweet(self, new_tweet):
        """
        tweet tweets a new tweet 


        :param new_tweet: tweets a entirely new tweet
        :type new_tweet: tweet
        """
        try:
            # tweet = self._t_auth.statuses.update(status = new_tweet)
            Utility.log('tweeter.autotweet',
                        'Wrote tweet: {0}'.format(new_tweet))
        except Exception as e:
            Utility.error('tweeter.autotweet',
                          'Failed to post tweet: {0}'.format(e))

    def retweet(self, id, tweet):
        """
        retweet Retweet a tweet with selected id


        :param id: twitter id from which the tweet is to be retweeted
        :type id: id
        :param tweet: tweet to be retweeted
        :type tweet: tweet
        """
        try:
            # self._ts_auth.statuses.retweet(id = id)
            Utility.log('tweeter.retweet',
                        'Retweeted tweet with id: {0} {1}'.format(id, tweet))
        except Exception as e:
            Utility.error('tweeter.retweet',
                          'Failed to retweer: {0}'.format(e))

    def _construct_new_tweet(self, model, seedword=None, prefix=None, suffix=None):
        """
        _construct_new_tweet Constructs a new tweet by adding prefix, suffix and limiting tweet to 280 characters


        :param model: markov model instance to be used
        :type model: model
        :param seedword: Seedword to be included in the tweet, defaults to None
        :type seedword: str, optional
        :param prefix: Predefind string to appear at the Start of the tweet, defaults to None
        :type prefix: str, optional
        :param suffix: predefined string that should appear at the end of string, defaults to None
        :type suffix: str, optional
        :return: gives out a tweet in form of string
        :rtype: str
        """
        max_words = 20
        response = ''
        while response == '' or len(response) > 280:
            response = model.generate_text(max_words, seedword)
            if prefix:
                response = '{0} {1}'.format(prefix, response)
            if suffix:
                response = '{0} {1}'.format(response, suffix)
            if len(response) > 280:
                max_words -= 1

        return response

    def excluding_conditions(self, tweet, black_list):
        """
        excluding_conditions Excludes tweets such as Hangup message, self-tweeted, retweet, reply, and user black-listed tweets.

        Filter conditions:
        1. Hangup message
        2. Self-tweeted
        3. Retweet
        4. Reply
        5. User black-listed    

        :param tweet: tweet to be approved
        :type tweet: tweet
        :param black_list: list of black-listed key words which will discard the tweet
        :type black_list: list
        :return: boolean to wether exclude or include the tweet
        :rtype: bool
        """
        exclude = False
        if 'hangup' in tweet.keys():
            exclude = True
        if tweet['user']['id_str'] == self._credentials['id_str']:
            exclude = True
        if 'retweeted_status' in tweet.keys():
            exclude = True
        if '@' in tweet['text'][0]:
            exclude = True
        if tweet['user']['screen_name'] in black_list:
            exclude = True
        return exclude

    def read_tweets(self, n=100):
        """
        read_tweets reads tweets with matching keywords stored in db/include.txt file via Twitter Stream


        :param n: number of tweets to be read, defaults to 100
        :type n: int, optional
        :return: filterd acceptable tweets according to modifiers
        :rtype: list
        """

        acceptable_tweets = []

        with open('../db/include.txt', 'r') as reader:
            include = reader.read()
        with open('../db/black_list.txt', 'r') as reader:
            black_list = reader.read()

        it = self._ts_auth.statuses.filter(track=include)
        tweet_count = 0
        while tweet_count < n:
            try:
                tweet = it.__next__()
            except StopIteration:
                continue
            if not self.excluding_conditions(tweet, black_list):
                acceptable_tweets.append(tweet)
                tweet_count += 1
        return acceptable_tweets

    @staticmethod
    def store(tweets, db='../db/db.csv'):
        """
        store Dumps necessary information of tweets into a csv file

        Savpath and filename of the database file, defaults to '../db/db.csv'
        :type db: str, optional
        """

        # Save desired attributes of tweet to a csv file
        with open(db, 'w', encoding="utf-8", newline='') as csv_file:

            fieldnames = ['id', 'rts', 'favs', 'text']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

            for tweet in tweets:
                try:
                    # Create a dictionary to hold all data
                    csv_dict = {}
                    csv_dict['id'] = tweet['id']
                    csv_dict['rts'] = tweet['retweet_count']
                    csv_dict['favs'] = tweet['favorite_count']

                    if 'extended_tweet' in tweet.keys():
                        csv_dict['text'] = tweet['extended_tweet']['full_text']
                    else:
                        csv_dict['text'] = tweet['text']

                except TypeError:
                    Utility.error('tweeter.store', 'Type Error encountered')

                # Write above dictionary as a row in csv file
                writer.writerow(csv_dict)
        Utility.log('tweeter.store',
                    'Wrote collected tweets to db {0}'.format(db))

    def amplify_tweets(self, n=1, timeout=60, db='../db/db.csv'):
        """
        amplify_tweets Amplifys stored tweet.

        Sort stored tweets based on their retweets number, re-tweet, then remove from db. 

        :param n: number of tweets to be amlified, defaults to 1
        :type n: int, optional
        :param timeout: interval between two tweets, defaults to 60
        :type timeout: int, optional
        :param db: path and filename of the database, defaults to '../db/db.csv'
        :type db: str, optional
        """

        dataframe = None
        if db is not None:
            dataframe = pandas.read_csv(db, header=None)
            dataframe.sort_values(1)

        count = 0
        while count < n and not dataframe.empty:

            # Obtain tweet and its corresponding tweet_id
            tweet = dataframe.iat[0, 3]
            tweet_id = dataframe.iat[0, 0]

            count += 1

            self._ts_lock.acquire(True)
            self.retweet(tweet_id, tweet)
            self._ts_lock.release()

            # Update data frame after tweet extracted
            dataframe = dataframe.drop(dataframe.index[0])
            time.sleep(timeout)

        # Write updated dataframe to db
        dataframe.to_csv(db, header=False, index=False)
