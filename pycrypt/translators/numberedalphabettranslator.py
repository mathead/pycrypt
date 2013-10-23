import translator
from .. import utils

class NumberedAlphabetTranslator(translator.Translator):
	def parseInput(self, cipher):
		if (type(cipher) != list):
			return map(int, utils.split(str(cipher)))
		return map(int, cipher)

	def translate(self, cipher):
		return "".join([utils.alphabet[(i % len(utils.alphabet)) - 1] for i in self.parseInput(cipher)])

	def encode(self, cipher):
		return " ".join([str(utils.alphabet.find(i) + 1) for i in cipher.upper()])