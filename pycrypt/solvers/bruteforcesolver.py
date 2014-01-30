import solver
from ..translators.caesartranslator import *
from ..keygenerators.numberkeygenerator import *
from ..keygenerators.keygenerator import *
from ..scorers.czechscorer import *

class BruteForceSolver(solver.Solver):
	"""Tries out all possible solutions"""

	def __init__(self, keyGenerator=NumberKeyGenerator(), translator=CaesarTranslator(), scorer=CzechScorer(), quiet=False):
		"""keyGenerator can be either KeyGenerator or iterable, to silence text output use quiet"""
		solver.Solver.__init__(self, keyGenerator, translator, scorer)
		if (quiet):
			self.printer = lambda *x: None
			self.lastPrint = lambda *x: None

	def solve(self, text=None, return_all_keys=False):
		best = (0.0, None)
		all_keys = []
		gen = self.keyGenerator
		if (isinstance(self.keyGenerator, KeyGenerator)): # otherwise iterable
			gen = self.keyGenerator.getAllKeys()

		for key in gen:
			score, ciphered_text = self.getScore(key, text)
			if (return_all_keys):
				all_keys.append((score, key))
			self.printer(key, score, ciphered_text)
			if (score > best[0]):
				best = (score, key)

		self.lastPrint(best[1], best[0], self.getScore(best[1], text)[1])
		if (return_all_keys):
			return sorted(all_keys, key=lambda x: -x[0])
		return best

	def printer(self, key, score, text=None):
		print ("Score: {:.5f}      Key: {:2}      Text: {}").format(score, "".join(key), text[:80])

	def lastPrint(self, key, score, text=None):
		print
		print "=====Best Solution====="
		print "Score:", score
		print "Key:", "".join(key)
		print "Text:", text[:100]

	def setKeyGenerator(self, keyGenerator):
		self.keyGenerator = keyGenerator

	def setStartingPoint(self, startingPoint):
		raise NotImplementedError()
