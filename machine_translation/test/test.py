import unittest

from translator import english_to_french, french_to_english


class Testtranslator(unittest.TestCase):
    def test1(self):
        # test for the translation of the world ‘Hello’ and ‘Bonjour’.
        self.assertEqual(english_to_french('Hello'), 'Bonjour')
        self.assertIsNone(english_to_french())


class TestDouble(unittest.TestCase):
    def test1(self):
        # test for the translation of the world  ‘Bonjour‘ and ‘Hello’.
        self.assertEqual(french_to_english('Bonjour'), 'Hello')
        self.assertIsNone(french_to_english())


unittest.main()
