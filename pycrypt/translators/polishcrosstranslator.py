from . import translator
from .. import utils
from collections import OrderedDict
import numpy as np

class PolishCrossTranslator(translator.Translator):
	"""Polish cross, Ch optional as argument, input: q1 -> A, c3 -> Z"""
	key = dict(zip(list('qweasdzxc'), range(9)))

	def __init__(self, using_ch=True):
		self.setUsingCh(using_ch)

	def setUsingCh(self, using_ch):
		if (using_ch):
			self.alphabet = utils.alphabetWithCh
		else:
			self.alphabet = utils.alphabet

	def parseInput(self, cipher):
		cipher = cipher.lower()
		cipher.replace(',', ' ')
		return cipher.split(" ")

	def translate(self, cipher):
		ret = ""
		for i in self.parseInput(cipher):
			if (len(i) == 2 and self.key.has_key(i[0])):
				ret += self.alphabet[self.key[i[0]] * 3 + int(i[1]) - 1] # moc velky
			else:
				if (i == ""):
					ret += " "
				else:
					ret += i
		return ret

	def encode(self, cipher):
		ret = ""
		key = list('qweasdzxc')
		for i in cipher:
			if (not str(i).upper() in self.alphabet):
				ret += i
			else:
				index = self.alphabet.index(str(i).upper())
				ret += key[int(index / 3)] + str((index % 3) + 1) + " "

		return ret[:-1]

	def graphicEncode(self, cipher, three_by_three_grid=False):
		"""Splits input to words, draws letters in words over each other.
		 If three_by_three_grid argument is False, 9x3 grid with individual letters in the polish cross will be used"""
		final_array = []
		seq = [['q', 'w', 'e'], ['a', 's', 'd'], ['z', 'x', 'c']]
		for line in utils.line_split(cipher):
			l = []
			for word in self.encode(line).split("  "):
				if (three_by_three_grid):
					c = np.zeros([3, 3])
				else:
					c = np.zeros([3, 9])

				for polish_char in word.split(" "):
					for a, x in enumerate(seq):
						for b, y in enumerate(x):
							if (y == polish_char[0]):
								if (three_by_three_grid):
									c[a][b] = 1
								else:
									c[a][b * 3 + int(polish_char[1]) - 1] = 1

				l.append(c)
			final_array.append(l)

		return utils.array_concat(final_array)