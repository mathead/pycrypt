import multiprocessing as mp
import dill
import itertools
from . import solver
from .geneticsolver import GeneticSolver
from ..translators.substitutiontranslator import *
from ..keygenerators.substitutionkeygenerator import *
from ..scorers.czechscorer import *
from .. import utils
import pprint


def mapper(solver):
    solver, text, iterations, log = dill.loads(solver)
    random.seed()  # since the environment is copied, we need to reinitialize the seed for each process
    res = solver.solve(text, iterations, return_all_keys=True)
    if log != None:
        return res, solver.log
    return res

class ThreadedGeneticSolver(solver.Solver):
    """Implements the island model using GeneticSolver"""

    def __init__(self, keyGenerator=SubstitutionKeyGenerator(), translator=SubstitutionTranslator(), scorer=CzechScorer(),
                 num_processes=None, migration_iterations=10, migration_size=10, quiet=False, log=False, **kwargs):
        """
        kwargs are simply passed to GeneticSolver.
        Special argument num_processes sets the number of islands created, None sets it to number of cores.
        migration_iterations sets how often migration (exchange of best individuals),
        migration_size sets the number of those individuals
        """

        solver.Solver.__init__(self, keyGenerator, translator, scorer)
        if (quiet):
            self.printer = lambda *x: None
            self.lastPrint = lambda *x: None

        self.printLength = 80
        self.num_processes = num_processes if num_processes else mp.cpu_count() # number of cores
        self.migration_iterations = migration_iterations
        self.migration_size = migration_size
        self.quiet = quiet
        self.log = [[] for i in range(self.num_processes)] if log else None
        self.kwargs = kwargs

        self.solvers = [GeneticSolver(self.keyGenerator, self.translator, self.scorer, quiet=i or quiet, log=log, **kwargs)
                        for i in range(self.num_processes)] # only one solver will not be quiet
        self.solvers[0].lastPrint = lambda *x: None

    def solve(self, text=None, iterations=0, return_all_keys=False):
        """Paralelized GeneticSolver's solve. Note that you can't interrupt the evolution as you could normally."""
        while (iterations != 1):
            iterations -= 1

            # we need to pickle all the needed information for the mapper function (as it is completely isolated)
            results = mp.Pool().map(mapper, [dill.dumps((s, text, self.migration_size, self.log)) for s in self.solvers])
            if self.log != None:
                results, logs = zip(*results)

            # exchange best individuals in cyclicly (island 1 sends to island2, island 2 to 3 and so on)
            best = results[0][0]
            for i, solver in enumerate(self.solvers):
                pop = [result[1] for result in results[i]]
                pop += [result[1] for result in results[(i+1) % len(results)][:self.migration_size]] # add new individuals
                solver.setStartingPoint(pop)

                if results[i][0][0] >= best[0]: # find best individual for printing
                    best = results[i][0]

            self.translator.setKey(best[1])
            translated = self.translator.translate(text)
            self.printer(best[1], best[0], translated, iterations)
            if self.log != None:
                for i in range(len(self.solvers)):
                    self.log[i].extend(logs[i])

        results = itertools.chain(*results)
        results = sorted(results, key=lambda x: -x[0])
        self.lastPrint(results[0][1], results[0][0], self.score(results[0][1], text)[1])
        if return_all_keys:
            return results
        return results[0]

    def printer(self, key, score, text=None, iterations=None):
        """Gets the best sample in population in every cycle"""
        print
        print("Migration! Best individual from all {} islands:".format(self.num_processes))
        print(("{:3}.      Score: {:.5f}      Text: {}").format(abs(iterations), score, text))#[:self.printLength]))
        if (type(key) == dict):
            print("Key:")
            utils.pprint_dict(key)
        else:
            print("Key:", key)
        print("===================================")
        print

    def setStartingPoint(self, startingPoint):
        for solver in self.solvers:
            solver.setStartingPoint(startingPoint)

    def lock(self, string, key=None):
        for solver in self.solvers:
            solver.lock(string, key)

    def plotLog(self):
        utils.plot_genetic_log_threaded(self.log)
