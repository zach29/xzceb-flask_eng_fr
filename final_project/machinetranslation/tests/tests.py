import unittest
from translator import english_to_french, french_to_english
import json


class TestTranslator(unittest.TestCase):
        

        def test_english_to_french(self):
                response = english_to_french("Hello")
                translation = response["translations"][0]["translation"]
                self.assertEqual(translation, "Bonjour")

        def test_english_to_french_null(self):
                self.assertIsNone(english_to_french(None))

        def test_french_to_english(self):
                response = french_to_english("Bonjour")
                translation = response["translations"][0]["translation"]
                self.assertEqual(translation, "Hello")     

        def test_french_to_english_null(self):
                self.assertIsNone(french_to_english(None))



if __name__ == '__main__':
    unittest.main()