import unittest
from substitutiontranslator import *
from .. import utils

class TestSubstitutionTranslator(unittest.TestCase):
    def setUp(self):
        self.ST = SubstitutionTranslator()
        key = dict(zip(utils.alphabet, utils.alphabet))
        key['A'], key['B'], key['C'] = "C", "A", "B"
        self.ST.setKey(key)

    def test_translate(self):
        self.assertEqual(self.ST.translate("ab c"), "CA B")

    def test_encode(self):
        self.assertEqual(self.ST.encode("abc"), "BCA")

    def test_parseInput(self):
        self.assertEqual(self.ST.parseInput("abc"), "ABC")

    def test_setKey(self):
        self.assertEqual(self.ST.key.keys(), list(utils.alphabet))

if __name__ == '__main__':
    unittest.main()