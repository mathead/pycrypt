import translator
import xortranslator

class MulXorTranslator(translator.Translator):
	"""Translator for multiple XOR cipher texts with same pad"""
	def __init__(self):
		self.xorTrans = xortranslator.XorTranslator()

	def translate(self, ciphers):
		self.xorTrans.setKey(self.key)
		return "".join([self.xorTrans.translate(c) for c in ciphers])