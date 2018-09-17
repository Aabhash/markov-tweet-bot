from markov_model import MarkovModel
from utility import Utility

# Create MarkovModel object to formulate tweets
model = MarkovModel()

# Read content from file
content = Utility.read_contents_from_file('../shakespeare.txt')

# Carve up a dictionary from read
model.create_dict(content)

# Generate text of size(n)
text = model.generate_text(30)

# print(model.corpus)
print(text)
