class TextProcessor:

    @staticmethod
    # def capitalize_i(word):
        # if ('.' in word[i-1] or word[i] == 'i'):
            # word[i].toUpper()

    @staticmethod
    def clean_grammar(text):
        for i in range(0, len(text)):
            if i == 0:
                text[i].upper()
        return text

