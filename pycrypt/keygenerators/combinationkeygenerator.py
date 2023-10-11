from .keygenerator import *
from ..translators.vigeneretranslator import *
from .. import utils
from math import ceil
import itertools as it
import copy
import random

class CombinationKeyGenerator(KeyGenerator):
	def __init__(self, alphabet=utils.alphabet, rand_func=lambda x: x ** 10, length_range=(1, 6), **kwargs):
		"""To be used with VigenereTranslator, generates combinations of the given set (alphabet)"""
		KeyGenerator.__init__(self, **kwargs)
		self.alphabet = list(alphabet)
		self.locks = {}
		self.randFunc = rand_func
		self.length_range = length_range

	def getRandomKey(self, length=None):
		"""If length is None, random from range is set"""
		if (length == None):
			length = random.randint(*self.length_range)
		key = [random.choice(self.alphabet) for i in range(length)]
		if isinstance(key, str):
			return "".join()
		return key

	def getAllKeys(self):
		"""Generator of all combinations from shortest to longest from length_range"""
		for i in range(self.length_range[0], self.length_range[1] + 1):
			for j in it.product(*([self.alphabet] * i)):
				yield j

	def mutateKey(self, key):
		"""Changes random number of elements, randomly changes length by 1"""
		ret = list(key)

		for i in range(len(ret)):
			rand = random.randint(1, 4 * len(ret))
			if (rand == 1 and len(ret)+1 <= self.length_range[1]):
				ret += random.choice(self.alphabet)
			elif (rand == 2 and len(ret)-1 >= self.length_range[0]):
				ret = ret[0:len(ret)-1]

		for i in range(int(ceil(self.randFunc(random.random()) * len(key)))):
			ret[random.choice(range(len(ret)))] = random.choice(self.alphabet)

		return ret 
