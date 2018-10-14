from markov_model import MarkovModel
from utility import Utility
from tweeter import Tweeter
import sys

'''
Load command line parameters
'''
def load_params():
    try:
        filename = sys.argv[2]
        keyword = sys.argv[3]
        pre = sys.argv[4]
        suf = sys.argv[5]
        n = sys.argv[6]
    except Exception:
        Utility.error('main','Error in passed parameters.')
    return filename, keyword, pre, suf, n


def main():
    """
    Tweeter object and related credentials
    """
    tweeter = Tweeter()

    c_key = ''
    c_secret = ''
    a_token = ''
    a_secret = ''

    """
    Login to twitter using above credentials
    """
    tweeter.login(c_key, c_secret, a_token, a_secret)

    try:
        load = sys.argv[1]
    except Exception:
        Utility.error('main','Error in passed parameters.')

    """
    Create MarkovModel object to formulate tweets
    """
    model = MarkovModel()
    try:
        # Load a already saved model
        if load in ['-l','-L']:
            filename, keyword, prefix, suffix, n_tweets = load_params()
            Utility.log('main', 'Loading model from file {0}'.format(filename))
            model.load('../model/m_blk_{0}'.format(filename))
            
            tweeter.start_tweeting(time=1, keywords=keyword.split(), prefix=prefix, suffix=suffix)
            tweeter._autoconstruct(model, int(n_tweets))
        # Carve up a dictionary from read
        elif load in ['-r','-R']:
            filename, keyword, prefix, suffix, n_tweets = load_params()
            Utility.log('main', 'Training model from file {0}, and saving.'.format(filename))
            model.read('../data/{0}.txt'.format(filename))
            model.save('../model/m_blk_{0}'.format(filename.split('.')[0]))

            tweeter.start_tweeting(time=1, keywords=keyword.split(), prefix=prefix, suffix=suffix)
            tweeter._autoconstruct(model, int(n_tweets))
        # Collect tweets and store to a database
        elif load in ['c','-C']:
            no = sys.argv[2]
            db_name = sys.argv[3]
            Utility.log('main', 'Collecting {0} tweets and saving then to {1}.'.format(no, db_name))
            tweeter.read_tweets(no)
            tweeter.store(db_name)
        # Load a number of tweets and amplify
        elif load in ['a', '-A']:
            no = sys.argv[2]
            timeout = sys.argv[3]
            Utility.log('main', 'Tweeting {0} tweets every {1} seconds'.format(no, timeout))
            tweeter.amplify_tweets(no, timeout)
        else:
            Utility.error('main', 'Invalid parameters')

        Utility.log('main', 'Exiting program ...')
    except KeyboardInterrupt:
        Utility.log('main', 'Terminating program ...')


if __name__ == '__main__':
    main()