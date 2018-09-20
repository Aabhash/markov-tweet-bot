from markov_model import MarkovModel
from utility import Utility
from tweeter import Tweeter

# Create MarkovModel object to formulate tweets
model = MarkovModel()

# Carve up a dictionary from read
model.read('../shakespeare.txt')
model.save('../model/m_blk_txt')

# Generate text of size(n)
text = model.generate_text(30)

# print(model.corpus)
print(text)

tweeter = Tweeter()
c_key = ''
c_secret = ''
a_token = ''
a_secret = ''

tweeter.login(c_key, c_secret, a_token, a_secret)
targetString = 'Shakespeare'
keywords = ['Romeo', 'Juliet']
prefix = None
suffix = '#cool'

# tweeter.t_areply_start(targetString, keywords=keywords, prefix=None, suffix='#TestBot')
tweeter.start_tweeting(days=0, hours=0, mins=0, keywords=keywords, prefix=None, suffix='#TestBot')
tweeter._autotweet()