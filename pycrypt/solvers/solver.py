from ..scorers.czechscorer import *

class Solver(object):
	"""Abstract class for connecting KeyGenerators, Scorers and optionally Translators"""
	
	def __init__(self, keyGenerator, translator=None, scorer=CzechScorer()):
		"""If translator is set to None, the keys themselves will be sent to the scorer"""
		self.keyGenerator = keyGenerator
		self.scorer = scorer
		self.translator = translator
		self.startingPoint = None

	def findBestKey(self, text=None):
		"""Find best scored key for the given text (if None, the key itself will be scored)
		Returns best (score, key) pair"""
		raise NotImplementedError()

	def setStartingPoint(self, startingPoint):
		"""Set where the findBestKey method should start (useful for continuing genetics)"""
		self.startingPoint = startingPoint

	def getScore(self, key, text=None, return_ciphered=True):
		if (text and self.translator):
			self.translator.setKey(key)
			text = self.translator.translate(text)
			if (return_ciphered):
				return self.scorer.getScore(text), text
			return self.scorer.getScore(text)

		if (return_ciphered):
			return self.scorer.getScore(key), text
		return self.scorer.getScore(key)

	def printer(self, key, score, text=None):
		"""Callback method for every key generated and scored"""
		pass

	def lastPrint(self, key, score, text=None):
		"""Callback method for last and best result"""
		pass