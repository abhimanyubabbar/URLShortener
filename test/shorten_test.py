import unittest
from shortener.shorten import UrlShortener

# Main Test Class for testing shorten functionality.


class TestShorten(unittest.TestCase):

    shortener = UrlShortener()

    def setUp(self):
        print('')
        print('@@ setup invoked @@')
        TestShorten.shortener = UrlShortener()

    def tearDown(self):
        print('@@ teardown invoked @@')

    def test_shortenUrl(self):

        print('Testing first encode')

        url = 'www.facebook.com'
        result = TestShorten.shortener.shortenUrl(url)
        self.assertEqual(result, '0', "First Encode")

    def test_originalUrl(self):

        print('Testing the process of de shortening url')

        url = 'https://github.com/babbarshaer'
        shortened_url = TestShorten.shortener.shortenUrl(url)

        original_url = TestShorten.shortener.originalUrl(shortened_url)
        self.assertEqual(url, original_url, 'Comparing de-shortened with original')

    def test_unknownUrl(self):

        print('Testing unknown url')
        shortened_url = '0'

        result = TestShorten.shortener.originalUrl(shortened_url)
        self.assertEqual('', result, "Unknown Url Test")

    def test_encodeBase62(self):

        print('Base Encoding62 Test.')
        input = 10
        expected_output = 'a'

        actual_output = TestShorten.shortener._encode(input)
        self.assertEqual(expected_output, actual_output, "Base62 encoding test.")

    def test_decodeBase62(self):

        print('Base62 Decoding Test.')
        test_input = 'a'
        expected_output = 10

        actual_output = TestShorten.shortener._decode(test_input)
        self.assertEqual(expected_output, actual_output, "Base62 decoding test.")

if __name__ == '__main__':
    unittest.main()
