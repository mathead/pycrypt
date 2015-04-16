import random
import itertools as it

def point1(parent1, parent2):
    """Basic 1 point crossover for lists"""
    if len(parent1) < 2:
        return []

    parent1, parent2 = list(parent1), list(parent2)
    point = random.randint(1, len(parent1) - 1)
    return [parent1[:point] + parent2[point:],
            parent2[:point] + parent1[point:]]

def point2(parent1, parent2):
    """Basic 2 point crossover for lists"""
    if len(parent1) < 3:
        return []

    parent1, parent2 = list(parent1), list(parent2)
    point1 = random.randint(1, len(parent1) - 2)
    point2 = random.randint(point1 + 1, len(parent1) - 1)
    return [parent1[:point1] + parent2[point1:point2] + parent1[point2:],
            parent2[:point1] + parent1[point1:point2] + parent2[point2:]]

def permutation(parent1, parent2):
    """
    Crossover for permutations, parents should be dicts.
    Inspired by order crossover 1 from http://www.cs.colostate.edu/~genitor/1995/permutations.pdf

    Note that crossing over two same individuals won't always return the same.
    """
    point1 = random.randint(1, len(parent1) - 2)
    point2 = random.randint(point1 + 1, len(parent1) - 1)

    cut = parent1.values()[point1:point2]
    filler = [x for x in parent2 if x not in cut]

    result = filler[point1+len(cut):] + cut + filler[:point1+len(cut)]
    return [dict(zip(parent1.keys(), result))]


class Tournament:
    """Basic tournament selector for crossovers"""
    def __init__(self, crossover_func=point2, tournament_size=20, crossovers=6):
        self.crossover_func = crossover_func
        self.tournament_size = tournament_size
        self.crossovers = crossovers

    def crossover(self, population):
        """Returns a list of new offsprings from population"""
        if len(population) < self.tournament_size:
            return []

        tournament = sorted(random.sample(population, self.tournament_size), key=lambda x: -x[0])[:self.crossovers*2]
        random.shuffle(tournament)
        ret = []
        for parents in it.izip_longest(*[iter(tournament)] * 2): # map it by pairs
            ret += self.crossover_func(parents[0][1], parents[1][1])
        return ret
