from markov_model import MarkovModel
from utility import Utility

# Create MarkovModel object to formulate tweets
model = MarkovModel()

# Carve up a dictionary from read
model.read('../shakespeare.txt')
model.save('../model/m_blk_txt')

# Generate text of size(n)
text = model.generate_text(30)

# print(model.corpus)
print(text)
