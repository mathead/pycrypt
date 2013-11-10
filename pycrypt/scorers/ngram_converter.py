# -*- coding: utf-8 -*-

from pprint import pprint
import pprint
import re
import sys
import codecs
import string
from unidecode import unidecode

NGRAM_LENGTH = 5
FILE_PATH = "czech-letters-5.txt"

alphabet = string.uppercase + " "

def normalize(istring):
	istring = istring.replace(" ", "")
	istring = istring.replace("&nbsp;", " ")
	istring = istring.upper()
	cont = False
	for i in istring:
		if (not i in alphabet):
			cont = True
	if (cont or istring == ""):
		return False
	return istring

first_pattern = re.compile(ur"ition:  (.*)  \(Count")
freq_pattern = re.compile(ur"[0-9]+ (.+) \(([0-9]+)\)")
final_dict = {}

with codecs.open(FILE_PATH, "r", "utf-8") as f:
	for i in f.read().split("Cond")[1:]:
		l = unidecode(i).split("\n")
		first_match = first_pattern.match(l[0])
		if (first_match):
			first = first_match.group(1)
		else:
			print "ERROR:", l[0]

		first = normalize(first)
		if (not first):
			continue

		print first

		for j in l[2:-1]:
			freq_match = freq_pattern.search(j)
			if (freq_match):
				letter, freq = freq_match.groups([1, 2])
				letter = normalize(letter)
				if (letter):
					key = first + letter
					if (len(key) == NGRAM_LENGTH):
						if (final_dict.has_key(key)):
							final_dict[key] += int(freq)
						else:
							final_dict[key] = int(freq)
			else:
				pass
				# print "ERROR:", j

	# pprint(final_dict)
	for i in final_dict:
		final_dict[i] /= float(564532247)
	final_arr = zip(final_dict.keys(), final_dict.values())
	# pprint(sorted(final_arr, key = lambda x: -x[1])[:10000])
	f2 = open("asd", "w")
	f2.write(pprint.pformat(sorted(final_arr, key = lambda x: -x[1])[:10000]))
	f2.close()
	input()
