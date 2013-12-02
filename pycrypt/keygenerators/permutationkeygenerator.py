from substitutionkeygenerator import *
from .. import utils
import random

class PermutationKeyGenerator(SubstitutionKeyGenerator):
	def __init__(self, sequence=utils.alphabet):
		"""Similar to SubstitutionTranslator, but returns just lists"""
		SubstitutionKeyGenerator.__init__(self, translator=None, alphabet=sequence)
		self.sequence = list(sequence)

	def getRandomKey(self):
		a = self.sequence[:]
		random.shuffle(a)
		return a

	def getAllKeys(self):
		"""Returns all permutations in lexicographic order (according to indexing in the given sequence)"""
		return super(PermutationKeyGenerator, self).getAllKeys(True)

	def mutateKey(self, key, rand_func=lambda x: x ** 5):
		"""Swaps random number of elements around"""
		return super(PermutationKeyGenerator, self).mutateKey(key, rand_func, True)
