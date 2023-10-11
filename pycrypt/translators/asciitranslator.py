from . import translator
from .. import utils

class ASCIITranslator(translator.Translator):
	"""Simple ASCII translation using unichr"""
	def parseInput(self, cipher):
		return map(int, utils.split(str(cipher)))

	def translate(self, cipher):
		return "".join([unichr(i) for i in self.parseInput(cipher)])

	def encode(self, cipher):
		return " ".join([str(ord(i)) for i in cipher])