class Scorer():
	"""Abstract class for scoring strings (i.e. language resemblance)"""
	
	def getScore(self, text):
		"""Get score of a string"""
		raise NotImplementedError()
