from . import translator
from .substitutiontranslator import *
from .. import utils

class VigenereTranslator(translator.Translator):
	"""Adds perpetually key letters to text (Caesar with longer keys)"""
	def __init__(self, key="A", ignore_nonletters=True):
		self.key = key
		self.ignore_nonletters = ignore_nonletters

	def parseInput(self, cipher):
		return cipher.upper()

	def translate(self, cipher, a_is_one = True):
		result = ""
		char_num = 0
		for i in self.parseInput(cipher):
			if (utils.alphabet.find(i) != -1):
				curr_key_char = utils.alphabet.find(self.key[char_num % len(self.key)]) + int(a_is_one)
				result += utils.alphabet[(utils.alphabet.find(i) + curr_key_char) % len(utils.alphabet)]
				char_num += 1
			else:
				if (not self.ignore_nonletters):
					char_num += 1
				result += i
		return result

	def encode(self, cipher):
		subs = SubstitutionTranslator()
		self.key = subs.translate(self.key)
		ret = self.translate(cipher, False)
		self.key = subs.encode(self.key)
		return ret

	# def setKey(self, key):
	# 	self.key = "".join(key).upper()