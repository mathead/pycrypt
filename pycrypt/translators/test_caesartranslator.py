import unittest
from .caesartranslator import *

class TestCaesarTranslator(unittest.TestCase):
    def setUp(self):
        self.CT = CaesarTranslator()

    def test_translate(self):
        self.CT.setKey(13)
        self.assertEqual(self.CT.translate("abc"), "NOP")
        self.assertEqual(self.CT.translate("ab c"), "NO P")

    def test_encode(self):
        self.CT.setKey(1)
        self.assertEqual(self.CT.encode("abc"), "ZAB")

    def test_parseInput(self):
        self.assertEqual(self.CT.parseInput("abc"), "ABC")

if __name__ == '__main__':
    unittest.main()