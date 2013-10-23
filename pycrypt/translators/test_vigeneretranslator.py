import unittest
from vigeneretranslator import *
from .. import utils
import numpy

class TestVigenereTranslator(unittest.TestCase):
    def setUp(self):
        self.T = VigenereTranslator("ABC")

    def test_translate(self):
        self.assertEqual(self.T.translate("AAABBB"), "BCDCDE")

    def test_encode(self):
    	self.assertEqual(self.T.encode("B C"), "A A")

if __name__ == '__main__':
    unittest.main()