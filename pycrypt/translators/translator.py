class Translator():
	"""Abstract class for translating standard ciphers (i.e. Morse Code)"""

	key = []

	def translate(self, *args):
		"""Base method for decoding a cipher"""
		raise NotImplementedError()

	def interactiveTranslate(self):
		"""For quick translating with each character typed from the user, type ! to remove last characters"""
		print("Interactive translation:")
		result = ""
		while True:
			try:
				i = input(" "*len(result))
				if (len(i) and i[0] == "!"):
					result = result[:-len(i)]
				else:
					result += self.translate(i)
				print(result)
			except KeyboardInterrupt:
				print(result)
				return result

	def encode(self, *args):
		"""Reversed translation"""
		raise NotImplementedError()

	def decode(self, *args):
		"""Just and alias for translate"""
		return self.translate(*args)

	def graphicEncode(self, *args):
		"""Return in numpy array for easy plotting"""
		raise NotImplementedError()

	def parseInput(self, cipher):
		"""Standardize input to a list, values preferably integers indexed from 0"""
		return cipher

	def setKey(self, key):
		self.key = key
