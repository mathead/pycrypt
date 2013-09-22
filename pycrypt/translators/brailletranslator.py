import translator
from .. import utils
from collections import OrderedDict
import numpy as np

class BrailleTranslator(translator.Translator):
	"""Braille, translation formats: swza is T (qw
												as
												zx)"""
	key  = {
			'': ' ',
			'q': 'A',
			'qa': 'B',
			'qw': 'C',
			'qws': 'D',
			'qs': 'E',
			'qaw': 'F',
			'qaws': 'G',
			'qas': 'H',
			'aw': 'I',
			'aws': 'J',
			'qz': 'K',
			'qaz': 'L',
			'qzw': 'M',
			'qzws': 'N',
			'qzs': 'O',
			'qazw': 'P',
			'qazws': 'Q',
			'qazs': 'R',
			'azw': 'S',
			'azws': 'T',
			'qzx': 'U',
			'qazx': 'V',
			'qazsx': 'W',
			'qzwx': 'X',
			'qzwsx': 'Y',
			'qzsx': 'Z'
		}


	def parseInput(self, cipher):
		cipher = cipher.lower()
		seq = list('qazwsx')
		cipher.replace(',', ' ')
		return ["".join(sorted(i, key=lambda a: seq.index(a))) for i in (cipher.split(" "))]

	def translate(self, cipher):
		return "".join([self.key.get(i, i) for i in self.parseInput(cipher)])

	def encode(self, cipher):
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