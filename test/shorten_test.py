import unittest
from shortener.shorten import UrlShortener

# Main Test Class for testing shorten functionality.


class TestShorten(unittest.TestCase):

    shortener = UrlShortener()

    def setUp(self):
        print('setup invoked')
        TestShorten.shortener = UrlShortener()

    def tearDown(self):
        print('teardown invoked')

    def test_shortenUrl(self):

        print('Testing first encode')

        url = 'www.facebook.com'
        result = TestShorten.shortener.shortenUrl(url)
        self.assertEqual(result, '0', "First Encode")

    def test_originalUrl(self):

        print('Testing the process of de shortening url')

        url = 'https://github.com/babbarshaer'
        shortenedUrl = TestShorten.shortener.shortenUrl(url)

        originalUrl = TestShorten.shortener.originalUrl(shortenedUrl)
        self.assertEqual(url, originalUrl, 'Comparing de-shortened with original')

    def test_unknownUrl(self):

        print('Testing unknown url')
        shortenedUrl = '0'

        result = TestShorten.shortener.originalUrl(shortenedUrl)
        self.assertEqual('', result, "Unknown Url Test")


if __name__ == '__main__':
    unittest.main()
