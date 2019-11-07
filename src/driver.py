from markov_model import MarkovModel
from utility import Utility
from tweeter import Tweeter
import sys


def load_params():
    """ Loads command line parameters

    Takes parameters as instructions on how to execute the script

    :return: returns filename, keyword, prefix, sufffix and numbers within a list
    :rtype: tuple in order of (filename, keyword, prefix, sufffix, numbers)
    """

    try:
        filename = sys.argv[2]
        keyword = sys.argv[3]
        pre = sys.argv[4]
        suf = sys.argv[5]
        n = sys.argv[6]
    except Exception:
        Utility.error('main', 'Error in passed parameters.')
    return filename, keyword, pre, suf, n


def main():
    """
    main the main driver code which logs into using the twitter credintials and executes the script according to the given modifier

    Options:
        -l : Load model from file. Use this if using an existing model. 
            Filename    : Name of pickle file to load markov model.  
            Keywords    : Seedwords which are an intergral part of tweet. Keywords may be single or multiple. 
            Prefix      : Word/s to start the tweet with. Prefix may be single or multiple words. 
            Suffix      : Word/s to add at the end of tweet. Suffix may be single or multiple words.
            num_tweets  : Number of tweets to be written.
        -r : Read file to create model. Use this if including your own text file.
            Filename    : Name of text file to construct markov model.  
            Keywords    : Seedwords which are an intergral part of tweet. Keywords may be single or multiple. 
            Prefix      : Word/s to start the tweet with. Prefix may be single or multiple words. 
            Suffix      : Word/s to add at the end of tweet. Suffix may be single or multiple words.
            num_tweets  : Number of tweets to be written.
        -c : Collect tweets from TwitterStream.
            no          : Number of tweets to collect.
        -a : Amplify tweets i.e. Retweet tweets stored using -c.   
            no          : Number of tweets to amplify.
            timeout     : Time to wait in seconds before retweeting. 


    logs into the twitter using the given credentials.

    If there is error it catches the exception and returns an exception message    
    """
    tweeter = Tweeter()

    # c_key = ''
    # c_secret = ''
    # a_token = ''
    # a_secret = ''
    # tweeter.login(c_key, c_secret, a_token, a_secret)

    try:
        load = sys.argv[1]
    except Exception:
        Utility.error('main', 'Error in passed parameters.')

    # Create MarkovModel object to formulate tweets
    model = MarkovModel()
    try:
        # Load a already saved model
        if load in ['-l', '-L']:
            filename, keyword, prefix, suffix, n_tweets = load_params()
            Utility.log('main', 'Loading model from file {0}'.format(filename))
            model.load('../model/m_blk_{0}'.format(filename))

            tweeter.start_tweeting(
                time=1, keywords=keyword.split(), prefix=prefix, suffix=suffix)
            tweeter._autoconstruct(model, int(n_tweets))
        # Carve up a dictionary from read
        elif load in ['-r', '-R']:
            filename, keyword, prefix, suffix, n_tweets = load_params()
            Utility.log(
                'main', 'Training model from file {0}, and saving.'.format(filename))
            model.read('../data/{0}.txt'.format(filename))
            model.save('../model/m_blk_{0}'.format(filename.split('.')[0]))

            tweeter.start_tweeting(
                time=1, keywords=keyword.split(), prefix=prefix, suffix=suffix)
            tweeter._autoconstruct(model, int(n_tweets))
        # Collect tweets and store to a database
        elif load in ['-c', '-C']:
            no = sys.argv[2]
            Utility.log(
                'main', 'Collecting {0} tweets and saving them to db.'.format(no))
            tweets = tweeter.read_tweets(int(no))
            Tweeter.store(tweets)
        # Load a number of tweets and amplify
        elif load in ['-a', '-A']:
            no = sys.argv[2]
            timeout = sys.argv[3]
            Utility.log(
                'main', 'Tweeting {0} tweets every {1} seconds'.format(no, timeout))
            tweeter.amplify_tweets(int(no), int(timeout))
        else:
            Utility.error('main', 'Invalid parameters')

        Utility.log('main', 'Exiting program ...')
    except KeyboardInterrupt:
        Utility.log('main', 'Terminating program ...')


if __name__ == '__main__':
    main()
