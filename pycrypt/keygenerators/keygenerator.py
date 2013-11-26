class KeyGenerator():
	"""Abstract class for generating and scoring keys for specific Translator"""

	def __init__(self, translator=None, scorer=None):
		pass

	def getRandomKey(self):
		"""Random key i.e. for starting genetic population"""
		raise NotImplementedError()

	def getAllKeys(self):
		"""Get all possible keys, list generator nejlepe""" ###############TODO