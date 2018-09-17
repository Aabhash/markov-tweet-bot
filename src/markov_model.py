import twitter
import random
from text_processor import TextProcessor

class MarkovModel:
    def __init__(self):
        self.corpus = {}
    
    # def clear_data():

    def create_dict(self, content, ngram=2):
        content = content.split()
        total_words = len(content) - ngram
        for word in range(total_words):
            key = tuple(i for i in content[word:word+ngram])
            if key in self.corpus:
                self.corpus[key].append(content[word+ngram])
            else:
                self.corpus[key] = [content[word+ngram]]
            
    
    # Return generated text
    def __get_result(self, n, word1, word2):
        resultant_text = []
        for i in range(n):
            resultant_text.append(word1)
            if (word1,word2) in self.corpus:
                word1, word2 = word2, random.choice(self.corpus[(word1, word2)])
        resultant_text.append(word2)
        return resultant_text

    def generate_text(self, keyword = "xyz good"):
        if not self.corpus:
            print('Corpus Empty')

        keyword = [keyword]
        keys = self.corpus 
        key_list = list(keys)
        random.shuffle(key_list)

        # Random seed
        seed = random.randint(0, len(list(keys)))
        word1, word2 = key_list[seed]
        # if seed != None: 
        #     while keyword:
        #         for i in range(len(keys)):
        #             if keyword[0] in key_list[i] or keyword[0].split() == key_list[i]:
        #                 word1, word2 = key_list[i]
        #                 keyword = []
        #                 break
        #         if keyword:
        #             keyword.pop(0)

        resultant_text = self.__get_result(140, word1, word2)
        # resultant_text = TextProcessor.clean_grammar(resultant_text)
        return resultant_text

model = MarkovModel()
with open('../shakespeare.txt', 'r') as reader:
    content = reader.read()
# print(content)
model.create_dict(content)
text = model.generate_text()
# print(model.corpus)
# print(' '.join(text))