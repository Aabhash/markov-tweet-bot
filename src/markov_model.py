import twitter
import random
from text_processor import TextProcessor

class MarkovModel:
    def __init__(self):
        self.corpus = {}
    
    # def clear_data():

    def create_dict(self, content, ngram=3):
        content = content.split()
        total_words = len(content) - ngram
        for word in range(total_words):
            key = tuple(i for i in content[word:word+ngram])
            if key in self.corpus:
                self.corpus[key].append(content[word+ngram])
            else:
                self.corpus[key] = [content[word+ngram]]
            
    
    # Return generated text
    def __get_result(self, n, words):
        resultant_text = []
        for i in range(n):
            temp = tuple(words)
            resultant_text.append(words[0])
            if temp in self.corpus:
                for i in range(len(words) - 1):
                    words[i] = words[i+1]
                words[len(words)-1] = random.choice(self.corpus[temp])
        resultant_text.append(words[len(words)-1])
        return resultant_text

    def generate_text(self):
        if not self.corpus:
            print('Corpus Empty')
            
        keys = self.corpus 
        key_list = list(keys)
        random.shuffle(key_list)
        seed = random.randint(0, len(list(keys)))
        words = list(key_list[seed])
        resultant_text = self.__get_result(140, words)
        return resultant_text

model = MarkovModel()
with open('../shakespeare.txt', 'r') as reader:
    content = reader.read()
# print(content)
model.create_dict(content)
text = model.generate_text()
# print(model.corpus)
print(' '.join(text))