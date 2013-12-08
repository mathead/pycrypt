import solver
from bruteforcesolver import *
from ..translators.substitutiontranslator import *
from ..keygenerators.substitutionkeygenerator import *
from ..scorers.czechscorer import *
from .. import utils

class GeneticSolver(solver.Solver):
	"""Uses own genetic algorithm, calls KeyGenerators mutateKey method"""

	def __init__(self, keyGenerator=SubstitutionKeyGenerator(), translator=SubstitutionTranslator(), scorer=CzechScorer(),
				 population_size=10, mutations=40, random_starting_population=1000, quiet=False):
		"""To silence text output use quiet, other params to tune the genetic algorithm"""
		solver.Solver.__init__(self, keyGenerator, translator, scorer)
		if (quiet):
			self.printer = lambda *x: None
			self.lastPrint = lambda *x: None

		self.population_size = population_size
		self.mutations = mutations
		self.random_starting_population = random_starting_population
		self.printLength = 80

		self.bruteForceSolver = BruteForceSolver(translator=translator, scorer=scorer, quiet=True) # for scoring population

	def findBestKey(self, text=None, iterations=0):
		"""Set iterations to 0 for infinite loop"""
		best = (0.0, None)
		tried = []

		if (self.startingPoint == None): # fill population from random samples
			self.bruteForceSolver.setKeyGenerator((self.keyGenerator.getRandomKey() for i in range(self.random_starting_population)))
			population = self.bruteForceSolver.findBestKey(text=text, return_all_keys=True)[:self.population_size]
		else:
			population = zip([self.getScore(i, text, False) for i in self.startingPoint], self.startingPoint)
			print population

		tried.extend(population)

		try:
			while (iterations != 1):
				iterations -= 1
				
				next_population = population[:]
				for sample in population:
					for i in range(self.mutations):
						mutant = self.keyGenerator.mutateKey(sample[1])
						while (mutant in tried):
							mutant = self.keyGenerator.mutateKey(sample[1])
						tried.append(mutant)
						next_population.append((self.getScore(mutant, text, False), mutant))

				population = sorted(next_population, key=lambda x: -x[0])[:self.population_size]

				key = population[0][1] # best in current
				score, ciphered_text = self.getScore(key, text)
				self.printer(key, score, ciphered_text, iterations)
				if (score > best[0]):
					best = (score, key)

		except (KeyboardInterrupt, SystemExit):
			print "Evolution interrupted! Setting starting point to continue"
			self.startingPoint = [best[1]]

		self.lastPrint(best[1], best[0], self.getScore(best[1], text)[1])
		return best

	def printer(self, key, score, text=None, iterations=None):
		"""Gets the best sample in population in every cycle"""
		print ("{:3}.      Score: {:.5f}      Text: {}").format(abs(iterations), score, text[:self.printLength])

	def lastPrint(self, key, score, text=None):
		print
		print "=====Best Solution====="
		print "Score:", score
		print "Key:"
		utils.pprint_dict(key)
		print "Text:", text

	def setStartingPoint(self, startingPoint):
		"""Starting population -> can be list"""
		if (type(startingPoint) == list):
			self.startingPoint = startingPoint
		else:
			self.startingPoint = [startingPoint]
