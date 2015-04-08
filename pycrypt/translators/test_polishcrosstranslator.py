import unittest
from polishcrosstranslator import *
from .. import utils
import numpy

class TestPolishCrossTranslator(unittest.TestCase):
    def setUp(self):
        self.T = PolishCrossTranslator(using_ch=True)

    def test_translate(self):
        self.assertEqual(self.T.translate("q1 q2  c3"), "AB Z")

    def test_encode(self):
        self.assertEqual(self.T.encode("B D"), "q2  w1")

    def test_graphicEncode(self):
        arr = numpy.vstack([numpy.ones([1, 9]), numpy.zeros([2, 9])])
        self.T.setUsingCh(False)
        self.assertTrue((self.T.graphicEncode(["abcdefghi"]) == arr).all())
        self.T.setUsingCh(True)


if __name__ == '__main__':
    unittest.main()