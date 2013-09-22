import string
import re
import numpy as np
import matplotlib.pyplot as plt

alphabet = string.uppercase

def split(string):
	return re.split('\W+', string)

def line_split(string):
	if (type(string) == str):
		return string.split("\n")
	else:
		return string

def array_concat(arrays):
	"""concats 3d numpy arrays to one big one, lines don't have to be the same size"""
	maxl = max([len(np.hstack(i)) for i in arrays])
	result = np.zeros([0, maxl])
	for i in arrays:
		line = np.hstack(i)

		zero_dim = [maxl - len(line)]
		if (line.ndim == 2):
			zero_dim[line.size / len(line), maxl - len(line)]

		a = np.hstack([line, np.zeros(zero_dim)])
		result = np.vstack([result, a])

	return result

def plot_array(arr):
	plt.imshow(arr, cmap=plt.cm.binary, interpolation='nearest')
	plt.xticks([]), plt.yticks([])
	plt.show()