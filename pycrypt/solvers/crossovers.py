import random

def point1(parent1, parent2):
    """Basic 1 point crossover for lists"""
    point = random.randint(1, len(parent1) - 1)
    return [parent1[:point] + parent2[point:],
            parent2[:point] + parent1[point:]]

def point2(parent1, parent2):
    """Basic 2 point crossover for lists"""
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
    def __init__(self, crossover_func=point1, tournament_size=20, crossovers=5):
        self.crossover_func = crossover_func
        self.tournament_size = tournament_size
        self.crossovers = crossovers

    def crossover(self, population):
        """Returns a list of new offsprings from population"""
        tournament = random.sample(population, self.tournament_size)
