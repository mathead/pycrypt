class Scorer():
	"""Abstract class for scoring strings (i.e. language resemblance)"""
	
	def score(self, text):
		"""Get score of a string"""
		raise NotImplementedError()
