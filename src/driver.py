from markov_model import MarkovModel
from utility import Utility
from tweeter import Tweeter
import sys

def main():
    # Load paramters from command line parameters
    try:
        load = sys.argv[1]
        filename = sys.argv[2]
        keyword = sys.argv[3]
        prefix = sys.argv[4]
        suffix = sys.argv[5]
        n_tweets = sys.argv[6]
    except Exception:
        Utility.error('main','Error in passed parameters.')
     
    """
    Create MarkovModel object to formulate tweets
    """
    model = MarkovModel()

    if load in ['-l','-L']:
        # Load a already saved model
        Utility.log('main', 'Loading model from file {0}'.format(filename))
        model.load('../model/m_blk_{0}'.format(filename))
    elif load in ['-r','-R']:
        # Carve up a dictionary from read
        Utility.log('main', 'Training model from file {0}, and saving.'.format(filename))
        model.read('../data/{0}.txt'.format(filename))
        model.save('../model/m_blk_{0}'.format(filename.split('.')[0]))
    else:
        Utility.error('main', 'Invalid parameters')

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
        tweeter.start_tweeting(days=0, hours=0, mins=1, keywords=keyword.split(), prefix=prefix, suffix=suffix)
        tweeter._autotweet(model, int(n_tweets))
        Utility.log('main', 'Exiting program ...')
    except KeyboardInterrupt:
        Utility.log('main', 'Terminating program ...')


if __name__ == '__main__':
    main()