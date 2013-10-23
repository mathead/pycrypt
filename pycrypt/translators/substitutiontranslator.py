import translator
from .. import utils
from collections import OrderedDict

class SubstitutionTranslator(translator.Translator):
	"""Basic substitution, default key reversed alphabet"""
	def __init__(self, key=utils.alphabet[::-1]):
		self.setKey(key)

	def setKey(self, key):
		if (type(key) in (dict, OrderedDict)):
			self.key = OrderedDict(sorted(key.items(), key=lambda t: t[0]))
		elif (type(key) in (str, list)):
			self.key = OrderedDict(zip(utils.alphabet, key))
		else:
			assert ValueError("Unknown key type")

	def parseInput(self, cipher):
		return cipher.upper()

	def translate(self, cipher):
		result = ""
		for i in self.parseInput(cipher):
			if (self.key.has_key(i)):
				result += self.key[i]
			else:
				result += i
		return result

	def encode(self, cipher):
		k = self.key
		self.setKey(dict(zip(self.key.values(), self.key.keys())))
		ret = self.translate(cipher)
		self.key = k
		return ret