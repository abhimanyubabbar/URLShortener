__author__ = 'babbarshaer'


class UrlShortener:
    """
    Original Url => Shortened Url | Shortened Url => Original Url
    """

    ALPHABET = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

    def __init__(self):
        self.map = dict()

    def shorten_url(self, url):
        """
        The function based on the url passed, creates a shortened url.
        :param url: url to be shortened.
        :return: shortened url
        """
        print(url)
        self.map[len(self.map)] = url
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
        Decoded the encoded string to the number.
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
