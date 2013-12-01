from substitutionkeygenerator import *
from .. import utils
import random

class PermutationKeyGenerator(SubstitutionKeyGenerator):
	def __init__(self, sequence=utils.alphabet):
		"""Similar to SubstitutionTranslator, but returns just lists"""
		SubstitutionKeyGenerator.__init__(self, translator=None, alphabet=sequence)
		self.sequence = sequence

	def getRandomKey(self):
		a = self.sequence[:]
		random.shuffle(a)
		return a

	def getAllKeys(self):
		"""Returns all permutations in lexicographic order (according to indexing in the given sequence)"""
		super(SubstitutionKeyGenerator, self).getAllKeys(True) # TODO: vola to KeyGenerator a ne SubstitutionKeyGenerator :(

	def mutateKey(self, key, rand_func=lambda x: x ** 5):
		"""Swaps random number of elements around"""
		super(SubstitutionKeyGenerator, self).getAllKeys(key, rand_func, True)
