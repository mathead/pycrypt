class Translator():
	"""Abstract class for translating standard ciphers (ie. Morse Code)"""
	key = []
	def translate(self):
		raise NotImplementedError()
	def interactiveTranslate(self):
		"""For quick translating with each character typed from the user, type ! to remove last characters"""
		print "Interactive translation:"
		result = ""
		while True:
			try:
				i = raw_input(" "*len(result))
				if (i[0] == "!"):
					result = result[:-len(i)]
				else:
					result += self.translate(i)
				print result
			except KeyboardInterrupt:
				print result
				return result

	def encode(self):
		"""Reversed translation"""
		raise NotImplementedError()
	def graphicEncode(self):
		"""Return in numpy array for easy plotting"""
		raise NotImplementedError()
	def parseInput(self, cipher):
		"""Standardize input to a list, values preferably integers indexed from 0"""
		return cipher
	def setKey(self, key):
		self.key = key