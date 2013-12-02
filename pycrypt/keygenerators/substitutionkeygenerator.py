from keygenerator import *
from ..translators.substitutiontranslator import *
from .. import utils
from math import ceil
import copy
import random

class SubstitutionKeyGenerator(KeyGenerator):
	def __init__(self, translator=SubstitutionTranslator(), alphabet=utils.alphabet):
		"""To be used with SubstitutionTranslator"""
		KeyGenerator.__init__(self, translator)
		self.alphabet = list(alphabet)

	def getRandomKey(self):
		a = self.alphabet[:]
		random.shuffle(a)
		return dict(zip(self.alphabet, a))

	def getAllKeys(self, _return_list=False):
		"""Returns all keys in lexicographic order (according to indexing in the given alphabet)"""
		perm = self.alphabet[:]
		while True:
			if (_return_list): # for PermutationKeyGenerator
				yield perm[:]
			else:
				yield dict(zip(self.alphabet, perm))

			k = None
			for i in range(len(perm)-1):
				if (self.alphabet.index(perm[i]) < self.alphabet.index(perm[i+1])):
					k = i
			if (k == None): # last permutation
				return
			for i in range(k+1, len(perm)):
				if (self.alphabet.index(perm[k]) < self.alphabet.index(perm[i])):
					l = i
			perm[k], perm[l] = perm[l], perm[k]
			perm = perm[:k+1] + list(reversed(perm[k+1:]))

	def mutateKey(self, key, rand_func=lambda x: x ** 5, _return_list=False):
		"""Swaps random number of elements around"""
		ret = copy.copy(key)

		for i in range(int(ceil(rand_func(random.random()) * len(ret)))):
			sample = self.alphabet
			if (_return_list):
				sample = range(len(ret))
			a, b = random.sample(sample, 2)
			ret[a], ret[b] = ret[b], ret[a]

		return ret
