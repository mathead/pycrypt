from substitutionkeygenerator import *
from .. import utils
import random

class PermutationKeyGenerator(SubstitutionKeyGenerator):
	def __init__(self, sequence=utils.alphabet):
		"""Similar to SubstitutionTranslator, but returns just lists"""
		SubstitutionKeyGenerator.__init__(self, alphabet=sequence)
		self.sequence = list(sequence)

	def getRandomKey(self):
		return super(PermutationKeyGenerator, self).getRandomKey(True)

	def getAllKeys(self):
		"""Returns all permutations in lexicographic order (according to indexing in the given sequence)"""
		return super(PermutationKeyGenerator, self).getAllKeys(True)

	def mutateKey(self, key, rand_func=lambda x: x ** 5):
		"""Swaps random number of elements around"""
		return super(PermutationKeyGenerator, self).mutateKey(key, rand_func, True)

	def lock(self, indx, value):
		"""Lock an index of the key, so that the other functions return only keys with the set value on the given index"""
		if (value not in self.alphabet):
			raise ValueError("Arguments not in sequence")
		self.locks[self.sequence[indx]] = value

	def unlock(self, indx):
		return self.locks.pop(self.sequence[indx])
