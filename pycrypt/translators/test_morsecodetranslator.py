import unittest
from morsecodetranslator import *
from .. import utils
import numpy

class TestMorseCodeTranslator(unittest.TestCase):
    def setUp(self):
        self.T = MorseCodeTranslator()

    def test_translate(self):
        self.assertEqual(self.T.translate(".-//-..."), "A B")
        self.assertEqual(self.T.translate("., ,..."), "AB")
        self.assertEqual(self.T.translate([[0,1],[1,0,0,0]]), "AB")

    def test_encode(self):
        self.assertEqual(self.T.encode("a b"), ".-//-...")

    def test_graphicEncode(self):
        self.assertTrue((self.T.graphicEncode("ab\nc") == numpy.array([[0,1,1,0,0,0],[1,0,1,0,0,0]])).all())

if __name__ == '__main__':
    unittest.main()