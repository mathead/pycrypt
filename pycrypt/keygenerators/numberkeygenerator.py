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
		