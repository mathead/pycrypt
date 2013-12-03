class KeyGenerator(object):
	"""Abstract class for generating keys for specific Translator"""

	def getRandomKey(self):
		"""Random key i.e. for starting genetic population"""
		raise NotImplementedError()

	def getAllKeys(self):
		"""Get all possible keys, python generator preferably"""
		raise NotImplementedError()

	def mutateKey(self, key):
		"""For genetics - get similar key"""
		raise NotImplementedError()
