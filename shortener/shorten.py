__author__ = 'babbarshaer'

import threading
import time

class UrlShortener:
    """
    Original Url => Shortened Url | Shortened Url => Original Url
    """

    ALPHABET = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

    def __init__(self):
        self.map = dict()
        self.reverse_map = dict()       # Create a reverse map, for holding the other resources.
        self.lock = threading.Lock()    # Get a lock instance

    def shorten_url(self, url):
        """
        The function based on the url passed, creates a shortened url.
        :param url: url to be shortened.
        :return: shortened url
        """
        print(url)
        self.lock.acquire()
        try:
            print('Lock Acquired')
            length = len(self.map)
            self.map[length] = url
            print('Map Updated with the resource.')

        finally:
            print('Going to release the lock')
            self.lock.release()

        return self._encode(len(self.map)-1)

    def _encode(self, num, alphabet=ALPHABET):
        """
        Main method performing the encoding the url to the shortened url.
        :param num: location of url in the map.
        :return: encoded string
        """
        if num == 0:
            return alphabet[0]
        arr = []
        base = len(alphabet)
        while num:
            rem = num % base
            num //= base
            arr.append(alphabet[rem])
        arr.reverse()
        return ''.join(arr)

    def original_url(self, shortened_url):
        """
        Get the original url stored based on the shortened url provided.
        :param shortened_url: shortUrl
        :return: originalUrl
        """
        print('Call to get original url for shortened url:' + shortened_url)

        loc = self._decode(shortened_url)
        print('Location: ' + str(loc))

        result = ''
        if loc < len(self.map):
            result = self.map[loc]

        return result

    def _decode(self, shortened_url, alphabet=ALPHABET):
        """
        Decoded the encoded string tself.get_length()o the number.
        :param shortened_url: encoded string
        :param alphabet: decoding base
        :return:
        """
        base = len(alphabet)
        strlen = len(shortened_url)
        result = 0

        loc = 0
        for char in shortened_url:
            power = (strlen - (loc + 1))
            result += alphabet.index(char) * (base ** power)
            loc += 1
        return result

    def print_map(self):
        """
        Simply print the information about the stored map.
        :return:
        """
        print('Going to print map size.')
        print(self.map)

    def get_length(self):
        return len(self.map)
