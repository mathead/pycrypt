import translator
from .. import utils
from collections import OrderedDict
import numpy as np

class BinaryTranslator(translator.Translator):
	startWithOne = False

	def __init__(self, start_with_one=False):
		self.startWithOne = start_with_one

	def setStartWithOne(self, b):
		self.startWithOne = b

	def parseInput(self, cipher):
		cipher = cipher.upper()
		return utils.split(cipher)

	def translate(self, cipher):
		ret = ""
		for i in self.parseInput(cipher):
			try:
				bin_char = ((5 - len(i)) * "0") + i
				num = int(self.startWithOne + 0)
				for j, k in enumerate(reversed(bin_char)):
					num += (2 ** j) * int(k)
				ret += utils.alphabet[num]
			except ValueError, IndexError:
				ret += i
		return ret

	def encode(self, cipher):
		ret = ""
		l = []
		for i in range(len(utils.alphabet)):
			num = ""
			for j in range(5):
				if (i + self.startWithOne) % (2 ** (j + 1)) >= 2 ** j:
					num = "1" + num
				else:
					num = "0" + num
			l.append(num)
		key = dict(zip(utils.alphabet, l))
		return " ".join([key.get(i, i) for i in cipher.upper()])

	def graphicEncode(self, cipher):
		final_array = []
		for line in utils.line_split(cipher):
			l = []
			for binary_char in self.encode(line).split(" "):
				l.append([int(i) for i in binary_char])
			final_array.append(l)

		return utils.array_concat(final_array)