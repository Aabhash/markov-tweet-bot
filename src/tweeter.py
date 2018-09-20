from markov_model import MarkovModel
from utility import Utility
import twitter
import time
from threading import Thread, Lock
import copy
import random
from text_processor import TextProcessor

class Tweeter:
    
    def __init__(self):

        # Tweet pesistance

        self._last_tweet_in = None
        self._last_tweet_out = None

        self._autotweet_flag = False
        
        # Auto tweet attributes
        self._keywords = None
        self._prefix = None
        self._suffix = None
    
        self._jitter = 1
        self._interval = 1

        # API Access
        self._oauth = None
        self._t_auth = None
        self._ts_auth =None

        self._t_lock = Lock()
        self._ts_lock = Lock()

        # Login
        self._logged_in = False
        self._credentials = None


    """
    Login to twitter using credentials provided
    """
    def login(self, c_key, c_secret, a_token, a_t_secret):
        self._oauth = twitter.OAuth(a_token, a_t_secret, c_key, c_secret)
        self._t_auth = twitter.Twitter(auth = self._oauth)
        self._ts_auth = twitter.TwitterStream(auth = self._oauth)
        self._logged_in = True

        self._credentials = self._t_auth.account.verify_credentials()

    """
    Start auto tweets
    """
    def start_tweeting(self, days =1, hours = 0, mins = 0, jitter = 0, keywords = None, prefix = None, suffix = None):
        for i in [days, hours, mins]:
            if i <= 0 or i == None: i = 0
        
        interval = (days * 1440) + (60 * hours) + mins
        if interval == 0: interval = 1440

        self._interval = interval
        self._jitter = jitter
        self._keywords = keywords
        self._prefix = prefix
        self._suffix = suffix

        self._autotweet_flag = True

    """
    Stop auto tweets 
    """
    def stop_tweeting(self):
        self._interval = None
        self._jitter = None
        self._keywords = None
        self._prefix = None
        self._suffix = None

        self._autotweet_flag = False

    """
    Obtain prefix to include in tweet 
    """
    def _get_prefix_in_tweet(self):        
        if self._prefix == None or type(self._prefix) in [str]:
            prefix = copy.deepcopy(self._prefix)
        elif type(self._prefix) in [list, tuple]:
            prefix = random.choice(self._prefix)
        else:
            prefix = None
            Utility.log('get_prefix_in_tweet', 'Not using prefix')
        return prefix

    """
    Obtain suffix to include in tweet 
    """
    def _get_suffix_in_tweet(self):
        if self._suffix == None or type(self._suffix) in [str]:
            suffix = copy.deepcopy(self._suffix)
        elif type(self._suffix) in [list, tuple]:
            suffix = random.choice(self._suffix)
        else:
            suffix = None
            Utility.log('get_suffix_in_tweet', 'Not using suffix')
        return suffix

    """
    Core tweeting logic
    """
    def _autotweet(self, model):
        while self._autotweet_flag:
            if self._logged_in and self._autotweet_flag:
                keyword = None
                if(self._keywords != None):
                    if type(self._keywords) in [str]:
                        keyword = self._keywords
                    else:
                        keyword = random.choice(self._keywords)
                    
                prefix = self._get_prefix_in_tweet()
                suffix = self._get_suffix_in_tweet()

                new_tweet = self._construct_tweet(model, seedword=keyword, prefix=prefix, suffix=suffix)
                self._t_lock.acquire(True)

                try:
                    # tweet = self._t_auth.statuses.update(status = new_tweet)
                    Utility.log('autotweet', 'Wrote tweet: {0}'.format(new_tweet))
                    # self._last_tweet_out = copy.deepcopy(tweet)
                except Exception as e:
                    Utility.error('autotweet', 'Failed to post tweet: {0}'.format(e))
                
                self._t_lock.release()

                jitter = random.randint(-self._jitter, self._jitter)
                interval = self._interval + jitter
                Utility.log('autotweet', 'Sleeping for {0} seconds'.format(interval))
                time.sleep(interval / 1000)


    """
    Construct tweet by adding prefix, suffix and limiting tweet to 140 characters
    """
    def _construct_tweet(self, model, seedword = None, prefix = None, suffix = None):
        max_words = 20
        response = ''
        while response == '' or len(response) > 140:
            response = model.generate_text(max_words, seedword)
            if prefix != None: 
                response = '{0} {1}'.format(prefix, response)
            if suffix != None:
                response = '{0} {1}'.format(response, suffix)
            if len(response) > 140:
                max_words -= 1

        return response