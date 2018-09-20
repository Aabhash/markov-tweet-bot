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
c_key = 'LV9wtszZNS27dyET3aoPcU4xp'
c_secret = '4Z1CWVKGIxQReLjXghWiYwbHnnaPGSBdnDy62dlJ3FDXG9hB52'
a_token = '132850584-JB4wjiYZrfrKpboRPORgVq9lvxY9PADq1pYOVeEg'
a_secret = '5xnhx2Wjj96T3lSPk8GCIqrK245NHRoX0inhwBVR07mCQ'

tweeter.login(c_key, c_secret, a_token, a_secret)
targetString = 'Shakespeare'
keywords = ['Romeo', 'Juliet']
prefix = None
suffix = '#cool'

tweeter.t_areply_start(targetString, keywords=keywords, prefix=None, suffix='#TestBot')
tweeter.start_tweeting(days=0, hours=19, mins=30, keywords=keywords, prefix=None, suffix='#TestBot')