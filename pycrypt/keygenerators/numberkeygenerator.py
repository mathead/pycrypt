from keygenerator import *
from ..translators.numberedalphabettranslator import *
import random

class NumberKeyGenerator(KeyGenerator):
	def __init__(self, translator=NumberedAlphabetTranslator(), max_number=26):
		"""To be used with NumberedAlphabetTranslator, max_number is -1 for list indexing"""
		KeyGenerator.__init__(self, translator)
		self.max_number = max_number

	def getRandomKey(self):
		return random.randint(0, self.max_number - 1)

	def getAllKeys(self):
		return xrange(self.max_number)

	def mutateKey(self, key, rand_func=lambda x: x ** 6):
		"""Change rand_func for different transformation after random.random"""
		return (key + rand_func(random.random())) % self.max_number
