import string
import re
import numpy as np
import matplotlib.pyplot as plt
from collections import OrderedDict

alphabet = string.ascii_uppercase
alphabetWithCh = list(string.ascii_uppercase)
alphabetWithCh.insert(8, 'CH')

def split(string):
    return re.split('\W+', string)

def line_split(string):
    if (type(string) == str):
        return string.split("\n")
    else:
        return string

def array_concat(raw_arrays):
    """Concats 2d numpy arrays to one big one, lines don't have to be the same size"""
    arrays = []
    for i in raw_arrays:
        h = np.hstack(i)
        if (h.ndim == 1):
            arrays.append(h)
        else:
            arrays.extend(h)

    maxl = max([len(i) for i in arrays])
    result = np.zeros([0, maxl])
    for i in arrays:
        line = np.hstack(i)

        zero_dim = [maxl - len(line)]

        a = np.hstack([line, np.zeros(zero_dim)])
        result = np.vstack([result, a])

    return result

def plot_array(arr):
    """Plots binary 2d numpy array"""
    plt.imshow(arr, cmap=plt.cm.binary, interpolation='nearest')
    plt.xticks([]), plt.yticks([])
    plt.show()

def get_frequency(string, freq_alphabet=alphabet, ratio=False):
    """Count frequency of given alphabet, if None, count every char. Set ratio True to divide by length"""
    if (freq_alphabet):
        string = string.upper()
        f = OrderedDict.fromkeys(freq_alphabet, 0.0)
        for c in string:
            if (f.has_key(c)):
                f[c] += 1
    else:
        f = {}
        for c in string:
            if (f.has_key(c)):
                f[c] += 1
            else:
                f[c] = 1.0

    if (ratio):
        suma = sum(f.values())
        for i in f:
            f[i] /= suma

    return f

def plot_dict(d):
    """Plots bar graph of dict (usually used with get_frequency)"""
    val = d
    plt.bar(range(len(val)), np.array(val.values()))
    plt.xticks(np.arange(len(val))+0.4, d.keys())
    plt.show()

def pprint_dict(d):
    """Prints dicts keys and values on top of each other"""
    keys = sorted(d.keys())
    values = [d[i] for i in keys]
    print "".join(keys)
    print "".join(values)

def plot_genetic_log(log):
    """Plots the max, min and avg fitness of the population"""
    max_ = [max(*[k[0] for k in i]) for i in log]
    min_ = [min(*[k[0] for k in i]) for i in log]
    avg = [np.mean([k[0] for k in i]) for i in log]
    plt.plot(max_, label='max', linewidth=2)
    plt.plot(avg, ':', label='avg')
    plt.plot(min_, ':', label='min')
    plt.xlabel("iteration")
    plt.ylabel("score")
    plt.legend(loc='lower right')
    plt.grid()
    plt.show()

def plot_genetic_log_threaded(log):
    """Plots each island individually"""
    for n, island in enumerate(log):
        plt.plot([max(*[k[0] for k in i]) for i in island], linewidth=2, label="Island " + str(n+1))

    plt.xlabel("iteration")
    plt.ylabel("score")
    plt.legend(loc='lower right')
    plt.grid()
    plt.show()