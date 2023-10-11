from . import unittest
from .. import utils
from .crossovers import *

class TestCrossovers(unittest.TestCase):
    def test_point1(self):
        key = list("QWERTYUIOP")
        self.assertEqual(point1(key, key)[0], key)
        self.assertNotEqual(point1(key, list(reversed(key)))[0], key)

    def test_point2(self):
        key = list("QWERTYUIOP")
        self.assertEqual(point2(key, key)[0], key)
        self.assertNotEqual(point2(key, list(reversed(key)))[0], key)

    def test_permutation(self):
        key = dict(zip(utils.alphabet, utils.alphabet))
        key2 = dict(zip(utils.alphabet, list(reversed(utils.alphabet))))
        self.assertEqual(len(set(permutation(key, key2)[0].values())), len(key))

if __name__ == '__main__':
    unittest.main()