from . import translator
from .. import utils
import numpy as np

class SemaphoreTranslator(translator.Translator):
	"""Semaphore, translation format: zx is A  (qwe
												a d
												zxc)"""
	key  = {
			'': ' ',
			'zx': 'A',
			'ax': 'B',
			'qx': 'C',
			'wx': 'D',
			'ex': 'E',
			'dx': 'F',
			'xc': 'G',
			'az': 'H',
			'qz': 'I',
			'wd': 'J',
			'wz': 'K',
			'ez': 'L',
			'dz': 'M',
			'zc': 'N',
			'qa': 'O',
			'wa': 'P',
			'ea': 'Q',
			'ad': 'R',
			'ac': 'S',
			'qw': 'T',
			'qe': 'U',
			'wc': 'V',
			'ed': 'W',
			'ec': 'X',
			'qd': 'Y',
			'dc': 'Z'
		}


	def parseInput(self, cipher):
		cipher = cipher.lower()
		seq = dict(zip(list('qweadzxc'), range(8)))
		cipher.replace(',', ' ')
		return ["".join(sorted(i, key=lambda a: seq.get(a, 100))) for i in (cipher.split(" "))]

	def translate(self, cipher):
		return "".join([self.key.get(i, i) for i in self.parseInput(cipher)])

	def encode(self, cipher):
		k = dict(zip(self.key.values(), self.key.keys()))
		return " ".join([k.get(i, i) for i in cipher.upper()])

	def graphicEncode(self, cipher):
		final_array = []
		seq = [['q', 'w', 'e'], ['a', 's', 'd'], ['z', 'x', 'c']]
		for line in utils.line_split(cipher):
			l = []
			for sem_char in self.encode(line).split(" "):
				c = np.zeros([3, 3])
				c[1, 1] = 1
				for i in sem_char:
					for a, x in enumerate(seq):
						for b, y in enumerate(x):
							if (i == y):
								c[a][b] = 1
				l.append(c)
			final_array.append(l)

		return utils.array_concat(final_array)