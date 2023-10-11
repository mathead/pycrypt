from . import crossovers

class KeyGenerator(object):
    """Abstract class for generating keys for specific Translator"""
    def __init__(self, crossover=crossovers.Tournament(), **kwargs):
        self.crossoverSelector = crossover

    def getRandomKey(self):
        """Random key i.e. for starting genetic population"""
        raise NotImplementedError()

    def getAllKeys(self):
        """Get all possible keys, python generator preferably"""
        raise NotImplementedError()

    def mutateKey(self, key):
        """For genetics - get similar key"""
        raise NotImplementedError()

    def crossover(self, population):
        """For genetics - get some new offsprings"""
        return self.crossoverSelector.crossover(population)
