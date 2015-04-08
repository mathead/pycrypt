import unittest
from semaphoretranslator import *
from .. import utils
import numpy

class TestSemaphoreTranslator(unittest.TestCase):
    def setUp(self):
        self.T = SemaphoreTranslator()

    def test_translate(self):
        self.assertEqual(self.T.translate("zx  ax xq"), "A BC")

    def test_encode(self):
        self.assertEqual(self.T.encode("d e"), "wx  ex")

    def test_graphicEncode(self):
        self.assertTrue((self.T.graphicEncode("ab") == numpy.array([[0, 0, 0, 0, 0, 0], [0, 1, 0, 1, 1, 0], [1, 1, 0, 0, 1, 0]])).all())

if __name__ == '__main__':
    unittest.main()