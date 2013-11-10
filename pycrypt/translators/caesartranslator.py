import translator
from .. import utils

class CaesarTranslator(translator.Translator):
	"""Simple alphabet rotation, default ROT13"""
	def __init__(self, key=13):
		self.key = key

	def parseInput(self, cipher):
		return cipher.upper()

	def translate(self, cipher):
		result = ""
		for i in self.parseInput(cipher):
			if (utils.alphabet.find(i) != -1):
				result += utils.alphabet[(utils.alphabet.find(i) + self.key) % len(utils.alphabet)]
			else:
				result += i
		return result

	def encode(self, cipher):
		self.key = -self.key
		ret = self.translate(cipher)
		self.key = -self.key
		return ret
