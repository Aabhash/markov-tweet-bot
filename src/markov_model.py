import twitter
import random
from text_processor import TextProcessor

class MarkovModel:
    def __init__(self):
        self.corpus = {}
    
    # def clear_data():


    def create_dict(self):
        content = "Hello okay done this is good xyz lel cool ."
        content = content.split()
        res = ()
        for i in range(len(content)-2):
            if i == len(content) - 2:
                pass
            else:   
                res = (content[i], content[i+1], content[i+2])
            print(res)

        for word in range(len(content)-2):
            print(word, content[word]) 
            key = (content[word], content[word+1])
            if word == len(content)-2:
                pass
            else:
                key = (content[word], content[word+1])
                if key in self.corpus:
                    self.corpus[key].append(content[word+2])
                else:
                    self.corpus[key] = [content[word+2]]
            

    
    def generate_text(self, keyword = "xyz good"):
        if not self.corpus:
            print('Corpus Empty')
        # if type(keyword) in [str]:
        #     keyword = [keyword]
        keyword = [keyword]
        print(keyword)
        keys = self.corpus
        print(keys)
        key_list = list(keys)
        print(key_list)
        random.shuffle(key_list)

        # Random seed
        seed = random.randint(0, len(list(keys)))
        print(seed)
        print(key_list[seed])
        word1, word2 = key_list[seed]
        print(word1, word2)
        if seed != None: 
            while keyword:
                for i in range(len(keys)):
                    if keyword[0] in key_list[i] or keyword[0].split() == key_list[i]:
                        word1, word2 = key_list[i]
                        seedword = []
                        break
                if keyword:
                    keyword.pop(0)
        
        resultant_text = []

        for i in range(140):
            resultant_text.append(word1)
            if (word1,word2) in self.corpus:
                possibilities = self.corpus[(word1,word2)]
                word1, word2 = word2, random.choice(possibilities)
            else:
                word1, word2 = word2, ''
        resultant_text.append(word2)

        # resultant_text = TextProcessor.clean_grammar(resultant_text)
        return resultant_text

model = MarkovModel()
model.create_dict()
text = model.generate_text()
print(text)