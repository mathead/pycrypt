import solver
from ..translators.CaesarTranslator import *
from ..keygenerators.numberkeygenerator import *
from ..keygenerators.keygenerator import *
from ..scorers.czechscorer import *

class BruteForceSolver(solver.Solver):
	"""Tries out all possible solutions"""

	def __init__(self, keyGenerator=NumberKeyGenerator(), translator=CaesarTranslator(), scorer=CzechScorer()):
		"""keyGenerator can be either KeyGenerator or iterable"""
		solver.Solver.__init__(keyGenerator, translator, scorer)
		self.startingPoint = 13

	def findBestKey(self, text=None, return_all_keys=False):
		best = (0.0, None)
		all_keys = []
		gen = self.keyGenerator
		if (type(self.keyGenerator) == KeyGenerator):
			gen = keyGenerator.getAllKeys()

		for key in gen:
			score = self.getScore(key, text)
			if (return_all_keys):
				all_keys.append((score, key))
			self.printer(key, score, text)
			if (score > best[0]):
				best = (score, key)

		self.lastPrint(best[1], best[0], text)
		if (return_all_keys):
			return sorted(all_keys, key=lambda x: x[0])
		return best

	def printer(self):
		pass