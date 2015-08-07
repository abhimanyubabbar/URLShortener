__author__ = 'babbarshaer'


class UrlShortener:
    """
    Based on the url provided, create a shortened string.
    """

    ALPHABET = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

    def __init__(self):
        self.map = dict()

    def shortenUrl(self, url):
        """
        The function based on the url passed, creates a shortened url.
        :param url: url to be shortened.
        :return: shortened url
        """
        print(url)
        self.map[len(self.map)] = url
        return self._encode(len(self.map))

    def _encode(self, num, alphabet=ALPHABET):
        """
        Main method performing the encoding the url in the shortened url.
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

    def originalUrl(self, shortenedUrl):
        """
        Get the original url stored based on the shortened url provided.
        :param shortenedUrl: shortUrl
        :return: originalUrl
        """
        print('Call to get original url for shortened url:' + shortenedUrl)
        loc = self._decode(shortenedUrl)

        print('Location: ' + loc)
        return self.map[loc]

    def _decode(self, string, alphabet=ALPHABET):
        """
        Decoded the encoded string to the number.
        :param string:
        :param alphabet:
        :return:
        """
        base = len(alphabet)
        strlen = len(string)
        num = 0

        idx = 0
        for char in string:
            power = (strlen - (idx + 1))
            num += alphabet.index(char) * (base ** power)
            idx += 1
        return num
