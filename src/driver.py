from markov_model import MarkovModel
from utility import Utility
from tweeter import Tweeter

"""
Create MarkovModel object to formulate tweets
"""
model = MarkovModel()

"""
Carve up a dictionary from read
"""
# model.read('../data/thor.txt')
# model.save('../model/m_blk_thor')

"""
Load a already saved model
"""
model.load('../model/m_blk_politics')

"""
Tweeter object and related credentials
"""
tweeter = Tweeter()
c_key = ''
c_secret = ''
a_token = '-'
a_secret = ''

"""
Login to twitter using above credentials
"""
tweeter.login(c_key, c_secret, a_token, a_secret)

keywords = ['']
prefix = ''
suffix = '#TestBot'

tweeter.start_tweeting(days=0, hours=0, mins=1, keywords=keywords, prefix=prefix, suffix=suffix)
tweeter._autotweet(model)