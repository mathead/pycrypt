from . import translator

class XorTranslator(translator.Translator):
	"""One time pad translator"""
	def translate(self, cipher):
		if len(cipher) > len(self.key):
			return "".join([chr(x ^ y) for (x, y) in zip(cipher[:len(self.key)], self.key)])
		else:
			return "".join([chr(x ^ y) for (x, y) in zip(cipher, self.key[:len(cipher)])])

	def encode(self, cipher):
		return self.translate(cipher)
