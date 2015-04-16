from keygenerator import *
from .. import utils
from math import ceil
import copy
import random
import crossovers

class SubstitutionKeyGenerator(KeyGenerator):
    def __init__(self, alphabet=utils.alphabet, rand_func=lambda x: x ** 6, weighted=None,
                 crossover=crossovers.Tournament(crossover_func=crossovers.permutation), **kwargs):
        """To be used with SubstitutionTranslator"""
        KeyGenerator.__init__(self, crossover=crossover, **kwargs)
        self.alphabet = list(alphabet)
        self.locks = {}
        self.randFunc = rand_func
        self.weighted = weighted

    def getRandomKey(self, _return_list=False):
        values = self._getLockedAlphabet()
        random.shuffle(values)

        ret = self._addLockedKeys(values)
        if (_return_list):
            return zip(*ret)[1]
        return dict(ret)

    def getAllKeys(self, _return_list=False):
        """Generator of all keys in lexicographic order (according to indexing in the given alphabet)"""
        perm = self._getLockedAlphabet()
        while True: # doesn't use itertools because of locking speed optimization
            ret = self._addLockedKeys(perm)
            if (_return_list): # for PermutationKeyGenerator
                yield zip(*ret)[1]
            else:
                yield dict(ret)

            k = None
            for i in range(len(perm)-1):
                if (self.alphabet.index(perm[i]) < self.alphabet.index(perm[i+1])):
                    k = i
            if (k == None): # last permutation
                return
            for i in range(k+1, len(perm)):
                if (self.alphabet.index(perm[k]) < self.alphabet.index(perm[i])):
                    l = i
            perm[k], perm[l] = perm[l], perm[k]
            perm = perm[:k+1] + list(reversed(perm[k+1:]))

    def mutateKey(self, key, temp=1, _return_list=False):
        """Swaps random number of elements around"""
        ret = copy.copy(key)
        inverse = dict(zip(ret.values(), ret.keys()))

        if (_return_list): # if locked key isn't what it is supposed to be
            for i in self.locks:
                j = self.alphabet.index(i)
                a = self.locks[i]
                b = ret[j]
                ret[ret.index(self.locks[i])] = b
                ret[j] = a
        else:
            bret = inverse
            for i in self.locks:
                ret[i], ret[bret[self.locks[i]]] = self.locks[i], ret[i]

        sample = self._getLockedKeys()
        if (_return_list):
            sample = range(len(ret))
            for lock in self.locks:
                sample.remove(self.alphabet.index(lock))

        for i in range(int(ceil(self.randFunc(random.random()) * len(self._getLockedAlphabet())))):
            if len(sample) < 2:
                return ret
            if self.weighted != None:
                a, b = self._getPairTemp(temp, sample, inverse)
            else:
                a, b = random.sample(sample, 2)
            ret[a], ret[b] = ret[b], ret[a]

        return ret

    def lock(self, element, value=None, key=None):
        """Lock an element of the key, so that the other functions return only keys with the set value"""
        if (value):
            if (element not in self.alphabet or value not in self.alphabet):
                raise ValueError("Arguments not in alphabet")
            self.locks[element] = value
        elif (key):
            self.locks[dict(zip(key.values(), key.keys()))[element]] = element

    def unlock(self, element):
        return self.locks.pop(element)

    def clearLock(self):
        self.locks.clear()

    def _getLockedAlphabet(self):
        values = self.alphabet[:]
        for i in self.locks:
            values.remove(self.locks[i])

        return values

    def _getLockedKeys(self):
        keys = self.alphabet[:]
        for i in self.locks:
            keys.remove(i)

        return keys

    def _addLockedKeys(self, values):
        keys = self._getLockedKeys()

        keys.extend(self.locks.keys())
        val = values[:]
        val.extend(self.locks.values())

        return sorted(zip(keys, val), key=lambda x: self.alphabet.index(x[0]))

    def _getWeightedChoice(self, weights, sample):
        # taken from http://stackoverflow.com/a/3679747/3254381 and slightly edited
        weights = [weights[x] for x in sample]
        r = random.random() * sum(weights)
        upto = 0
        for c, w in zip(sample, weights):
            if upto + w > r:
                return c
            upto += w

    def _getWeightedPair(self, weights, sample):
        first = self._getWeightedChoice(weights, sample)
        sample.remove(first)

        return first, self._getWeightedChoice(weights, sample)

    def _getPairTemp(self, temp, sample, inverse):
        """
        Get keys with higher frequency more or less often according to temperature.
        temp = 1 no weights, temp = 2 take more frequent more often, temp = 0 take less frequent more often
        """
        freq = max(0, temp - 1)
        norm = 1 - abs(temp - 1)
        inv = max(0, 1 - temp)

        # we have to invert the key, because the weights are for the values, not keys
        weights = {key: self.weighted[inverse[key]] * (freq + inv) + norm for key in sample}
        return self._getWeightedPair(weights, sample[:])

