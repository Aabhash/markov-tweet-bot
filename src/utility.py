class Utility:

    @staticmethod
    def read_contents_from_file(filename):
        with open(filename, 'r') as reader:
            content = reader.read()
        return content