import unittest

from translator import english_to_french, french_to_english

class TestEnglish(unittest.TestCase):
    def test1(self):
        self.assertEqual(english_to_french(""), "")
        self.assertEqual(english_to_french('Hello'),'Bonjour')
        self.assertNotEqual(english_to_french('Thanks'), 'Bonjour')
    
class TestFrench(unittest.TestCase):
    def test1(self):
        self.assertEqual(french_to_english(""), "" )
        self.assertEqual(french_to_english('Bonjour'), 'Hello')
        self.assertNotEqual(french_to_english('Merci'), 'Hello')

unittest.main()