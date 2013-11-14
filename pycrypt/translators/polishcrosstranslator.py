import translator
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
			if (not i in self.alphabet):
				ret += i
			else:
				index = self.alphabet.index(i)
				ret += key[int(index / 3)] + str((index % 3) + 1)

		return ret

	def graphicEncode(self, cipher):
		"""Splits input to words, draws letters in words over each other"""
		final_array = []
		seq = [['q', 'w', 'e'], ['a', 's', 'd'], ['z', 'x', 'c']]
		for line in utils.line_split(cipher):
			l = []
			for braille_char in self.encode(line).split(" "): ##############TODO
				c = np.zeros([3, 2])
				for i in braille_char:
					for a, x in enumerate(seq):
						for b, y in enumerate(x):
							if (i == y):
								c[a][b] = 1
				l.append(c)
			final_array.append(l)

		return utils.array_concat(final_array)