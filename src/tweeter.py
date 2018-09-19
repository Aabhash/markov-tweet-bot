from markov_model import MarkovModel
from utility import Utility
import twitter

class Tweeter:
    
    def __init__(self):
        # Tweet data structure
        self._a_repl_db = {}
        self._db = {}

        # Auto Reply attributes
        self._targetstring = None
        
        self._auto_keywords = None
        self._auto_tweetprefix = None
        self._auto_tweetsuffix = None
    
        self._maxconvdepth = None
        self._mindelay = None

        self._autoreply = False
        self._autotweet = False
        
        # Auto tweet attributes
        self._keywords = None
        self._tweetprefix = None
        self._tweetsuffix = None
    
        self._jitter = None
        self._interval = None

        # API Access
        self._oauth = None
        self._t_auth = None
        self._ts_auth =None


    """
    Login to twitter using credentials provided
    """
    def login(self, c_key, c_secret, a_token, a_t_secret):
        self._oauth = twitter.OAuth(a_t, a_t_secret, c_key, c_secret)
        self._t_auth = twitter.Twitter(auth = self._oauth)
        self._ts_auth = twitter.TwitterStream(auth = self._oauth)

    """
    Start auto tweets
    """
    def start_tweeting(self, corpus, days =1, hours = 0, mins = 0, jitter = 0, keywords = None, prefix = None, suffix = None):
        for i in [days, hours, mins]:
            if i <= 0 or i == None: i = 0
        
        interval = (days * 1440) + (60 * hours) + mins
        if interval == 0: interval = 1440

        self._db = corpus
        self._interval = interval
        self._jitter = jitter
        self._keywords = keywords
        self._prefix = prefix
        self._suffix = suffix

        self._autotweet = True

    """
    Stop auto tweets 
    """
    def stop_tweeting(self):
        self._db = {}
        self._interval = None
        self._jitter = None
        self._keywords = None
        self._prefix = None
        self._suffix = None

        self._autotweet = False