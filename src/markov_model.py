import twitter
import random
# from text_processor import TextProcessor


class MarkovModel:
    def __init__(self):
        self.corpus = {}


    """
    Create a dictionary of (key,value) pairs where key is n-gram configuration 
    """

    def create_dict(self, content, ngram=3):

        content = content.split()
        total_words = len(content) - ngram

        for word in range(total_words):
            # Set up key as tuples of n word grams
            key = tuple(i for i in content[word:word + ngram])
            # Append word to the value in (key,value) dictionary pair
            # Add new (key,value) pair if list does not exist
            if key in self.corpus:
                self.corpus[key].append(content[word + ngram])
            else:
                self.corpus[key] = [content[word + ngram]]

    """
    Return text by appending words
    """

    def __get_text(self, n_length, words):

        resultant_text = []
        word_size = len(words) - 1

        # Contruct a text of size n words
        for ind in range(n_length):
            ngrams = tuple(words)
            resultant_text.append(words[0])

            # If words exist as key-words in corpus, shift by one word 
            # Then select random word from the list of words that follow key-words 
            if ngrams in self.corpus:
                words[:word_size] = words[1:word_size + 1]
                words[word_size] = random.choice(self.corpus[ngrams])

        resultant_text.append(words[word_size])
        return ' '.join(resultant_text)

    """
    Generate a text of size n.
    """

    def generate_text(self, text_length):
        if not self.corpus: print('Corpus Empty')

        # Convert corpus dictionary into a list of word-components
        word_components = list(self.corpus)
        random.shuffle(word_components)

        # Get random integer to obtain one word component to start resultant sentence
        rand_int = random.randint(0, len(list(self.corpus)))
        seed_words = list(word_components[rand_int])
        
        # Obtain resultant sentence of length n, commencing from seed words
        resultant_text = self.__get_text(text_length, seed_words)
        
        return resultant_text