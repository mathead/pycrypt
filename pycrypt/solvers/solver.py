from ..scorers.czechscorer import *

class Solver(object):
	"""Abstract class for connecting KeyGenerators, Scorers and optionally Translators"""
	
	def __init__(self, keyGenerator, translator=None, scorer=CzechScorer()):
		"""If translator is set to None, the keys themselves will be sent to the scorer"""
		self.keyGenerator = keyGenerator
		self.scorer = scorer
		self.translator = translator
		self.startingPoint = None

	def solve(self, text=None):
		"""Find best scored key for the given text (if None, the key itself will be scored)
		Returns best (score, key) pair"""
		raise NotImplementedError()

	def setStartingPoint(self, startingPoint):
		"""Set where the solve method should start (useful for continuing genetics)"""
		self.startingPoint = startingPoint

	def score(self, key, text=None, return_ciphered=True):
		if (text and self.translator):
			self.translator.setKey(key)
			text = self.translator.translate(text)
			if (return_ciphered):
				return self.scorer.score(text), text
			return self.scorer.score(text)

		if (return_ciphered):
			return self.scorer.score(key), text
		return self.scorer.score(key)

	def printer(self, key, score, text=None):
		"""Callback method for every key generated and scored"""
		pass

	def lastPrint(self, key, score, text=None):
		"""Callback method for last and best result"""
		pass
