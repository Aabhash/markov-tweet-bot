import os


class Utility:

    @staticmethod
    def read_contents_from_file(filename):
        """
        read_contents_from_file method which reads contents from a file

        method which will open a given file name and returns it's content in a string format

        :param filename: name of the file to be read
        :type filename: str
        :return: content inside the given file
        :rtype: str
        """
        with open(filename, 'r', encoding="utf8") as reader:
            content = reader.read()
        return content

    @staticmethod
    def error(method, message):
        """
        error method to display an error message

        :param method: the method where an error occured
        :type method: str
        :param message: Error message
        :type message: str
        :raises Exception: when an error message is passed it raises an exception
        """
        raise Exception('Error :- [{0}] {1}'.format(method, message))

    @staticmethod
    def check_integrity(filename):
        """
        check_integrity method to check if the file specified exists or not

        :param filename: name of the file to be checked
        :type filename: str
        :return: returns the boolean to indicate the existance of the file
        :rtype: bool
        """
        filepath_exists = os.path.isfile(filename)
        return filepath_exists

    @staticmethod
    def log(method, message):
        """
        log method to display log messages on the terminal


        :param method: the method where the log originated from
        :type method: str
        :param message: Log message
        :type message: str
        """
        print('Log Message :- [{0}] {1}'.format(method, message))
