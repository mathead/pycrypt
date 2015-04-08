import unittest
from binarytranslator import *
from .. import utils
import numpy

class TestBinaryTranslator(unittest.TestCase):
    def setUp(self):
        self.T = BinaryTranslator()

    def test_translate(self):
        self.assertEqual(self.T.translate("0 1 00010"), "ABC")

    def test_encode(self):
        self.assertEqual(self.T.encode("a b"), "00000   00001")

    def test_graphicEncode(self):
        self.assertTrue((self.T.graphicEncode("a\nb") == numpy.array([[0, 0, 0, 0, 0], [0, 0, 0, 0, 1]])).all())

if __name__ == '__main__':
    unittest.main()