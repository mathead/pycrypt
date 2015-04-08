import unittest
from brailletranslator import *
from .. import utils
import numpy

class TestBrailleTranslator(unittest.TestCase):
    def setUp(self):
        self.T = BrailleTranslator()

    def test_translate(self):
        self.assertEqual(self.T.translate("q  qazs qwsxz"), "A RY")

    def test_encode(self):
        self.assertEqual(self.T.encode("a b"), "q  qa")

    def test_graphicEncode(self):
        self.assertTrue((self.T.graphicEncode("ab") == numpy.array([[1, 0, 1, 0], [0, 0, 1, 0], [0, 0, 0, 0]])).all())

if __name__ == '__main__':
    unittest.main()