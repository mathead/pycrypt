import translator
from .. import utils
from collections import OrderedDict
import numpy as np

class MorseCodeTranslator(translator.Translator):
	"""Morse Code, translation formats: .-//-... ; ., ,... ; [[0,1],[1,0,0,0]]"""
	key  = {
			'': ' ',
			'.----.': '\'',
			'-.--.-': ')',
			'-.--.-': '(',
			'-....-': '-',
			'--..--': ',',
			'-..-.': '/',
			'.-.-.-': '.',
			'.----': '1',
			'-----': '0',
			'...--': '3',
			'..---': '2',
			'.....': '5',
			'....-': '4',
			'--...': '7',
			'-....': '6',
			'----.': '9',
			'---..': '8',
			'-.-.-.': ';',
			'---...': ':',
			'..--..': '?',
			'.-': 'A',
			'-.-.': 'C',
			'-...': 'B',
			'.': 'E',
			'-..': 'D',
			'--.': 'G',
			'..-.': 'F',
			'..': 'I',
			'....': 'H',
			'-.-': 'K',
			'.---': 'J',
			'--': 'M',
			'.-..': 'L',
			'---': 'O',
			'-.': 'N',
			'--.-': 'Q',
			'.--.': 'P',
			'...': 'S',
			'.-.': 'R',
			'..-': 'U',
			'-': 'T',
			'.--': 'W',
			'...-': 'V',
			'-.--': 'Y',
			'-..-': 'X',
			'--..': 'Z',
			'..--.-': '_',
		}


	def parseInput(self, cipher):
		if (type(cipher) == list):
			d = {1: '-', 0: '.'}
			ret = []
			for i in cipher:
				ret.append("".join([d[j] for j in i]))
			return ret

		if (type(cipher) == str):
			cipher = cipher.replace(" ", "/")
			cipher = cipher.replace(",", "-")
			return cipher.split("/")

	def translate(self, cipher):
		return "".join([self.key.get(i, i) for i in self.parseInput(cipher)])

	def encode(self, cipher):
		k = dict(zip(self.key.values(), self.key.keys()))
		return "/".join([k.get(i, i) for i in cipher.upper()])

	def graphicEncode(self, cipher, gkey={"-": [1], ".": [0]}):
		"""change gkey dict to other . and - representations (ie. '-' can be [1, 1, 1])"""
		k = dict(zip(self.key.values(), self.key.keys()))
		final_array = []
		for i in utils.line_split(cipher.upper()):
			line = []
			for j in i:
				char = []
				for morse_char in k.get(j, []):
					char.extend(gkey[morse_char])
				line.append(char)
			final_array.append(line)

		return utils.array_concat(final_array)