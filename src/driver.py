from markov_model import MarkovModel
from utility import Utility
from tweeter import Tweeter

# Create MarkovModel object to formulate tweets
model = MarkovModel()

# Carve up a dictionary from read
model.read('../thor.txt')
model.save('../model/m_blk_txt')

tweeter = Tweeter()
c_key = ''
c_secret = ''
a_token = ''
a_secret = ''

tweeter.login(c_key, c_secret, a_token, a_secret)

keywords = ['THOR', 'Banner']
prefix = ''
suffix = '#Avengers'

# tweeter.t_areply_start(targetString, keywords=keywords, prefix=None, suffix='#TestBot')
tweeter.start_tweeting(days=0, hours=0, mins=0, keywords=keywords, prefix=prefix, suffix=suffix)
# print(model.corpus)
tweeter._autotweet(model)