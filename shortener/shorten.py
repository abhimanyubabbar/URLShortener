__author__ = 'babbarshaer'


class UrlShortener:
    """
    Based on the url provided, create a shortened string and vice versa.
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

    def originalUrl(self, shortenedUrl):
        """
        Get the original url stored based on the shortened url provided.
        :param shortenedUrl: shortUrl
        :return: originalUrl
        """
        print('Call to get original url for shortened url:' + shortenedUrl)
        loc = self._decode(shortenedUrl)

        print('Location: ' + str(loc))
        return self.map[loc]

    def _decode(self, shortenedUrl, alphabet=ALPHABET):
        """
        Decoded the encoded string to the number.
        :param shortenedUrl: encoded string
        :param alphabet: decoding base
        :return:
        """
        base = len(alphabet)
        strlen = len(shortenedUrl)
        result = 0

        loc = 0
        for char in shortenedUrl:
            power = (strlen - (loc + 1))
            result += alphabet.index(char) * (base ** power)
            loc += 1
        return result
