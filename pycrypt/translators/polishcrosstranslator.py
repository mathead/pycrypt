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
		for i in cipher:
			ret += self.key[i[0]] * 3 + i[1] 
		return ret

	def encode(self, cipher):
		###################TODO
		k = dict(zip(self.key.values(), self.key.keys()))
		return " ".join([k.get(i, i) for i in cipher.upper()])

	def graphicEncode(self, cipher):
		final_array = []
		seq = [['q', 'w'], ['a', 's'], ['z', 'x']]
		for line in utils.line_split(cipher):
			l = []
			for braille_char in self.encode(line).split(" "):
				c = np.zeros([3, 2])
				for i in braille_char:
					for a, x in enumerate(seq):
						for b, y in enumerate(x):
							if (i == y):
								c[a][b] = 1
				l.append(c)
			final_array.append(l)

		return utils.array_concat(final_array)