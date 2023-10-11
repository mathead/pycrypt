from . import scorer
from .. import utils
from unidecode import unidecode
# import cgetngramfrequencies

class LanguageScorer(scorer.Scorer):
	"""Scorer for languages based on N-grams and words"""

	words = None
	minWordLen = 3
	maxWordLen = 10
	log = False
	ngramWeights = None
	wordWeight = 0
	unidec = True

	def setIdealNgramFrequencies(self, freqs):
		self.idealNgramFrequencies = freqs
		self.idealNgramsKeySets = [set(i.keys()) for i in freqs]
		self.ngramLens = [len(list(i.keys())[0]) for i in freqs]
		if (self.ngramWeights == None):
			self.ngramWeights = [1] * len(freqs)

	def loadWordList(self, path, minwordlen = 3, maxwordlen = 10):
		"""Load words from file, 1 word per line"""
		self.minWordLen = minwordlen
		self.maxWordLen = maxwordlen
		self.words = set([line.strip().upper() for line in open(path)])

	def setWeights(self, ngram_weights, word_weight = 0):
		"""Score multipliers, ngram_weights is list corresponding to ideal frequencies
		when something is 0, it's ignored when scoring"""
		self.ngramWeights = ngram_weights
		self.wordWeight = word_weight

	def getNgramFrequencies(self, text, length):
		"""Get dictionary of frequencies of N-grams (of given length)"""
		# return cgetngramfrequencies.getNgramFrequencies(text, length)
		d = {}
		for i in range(len(text) + 1 - length):
			sub = text[i:i+length]
			if sub in d:
				d[sub] += 1
			else:
				d[sub] = 1

		# for i in d:
		# 	d[i] /= len(text)

		return d

	def scoreNgrams(self, text):
		scores = []
		for i, ideal_freq in enumerate(self.idealNgramFrequencies):
			scores.append(0.0)
			if (self.ngramWeights[i]): # 0 is to ignore

				text_freq = self.getNgramFrequencies(text, self.ngramLens[i])

				for ngram in list(self.idealNgramsKeySets[i] & set(text_freq.keys())): # get only mutual ngrams
					scores[i] += ideal_freq[ngram] * (text_freq[ngram] / float(len(text))) # weird equation, but it works

		return scores
		
	def scoreWords(self, text):
		if (self.maxWordLen == 0 or self.words == None):
			return 0

		s = text
		pts = 0.0
		for length in range(self.minWordLen, self.maxWordLen):
			for pos in range(len(s) - 1 - length):
				if (s[pos:pos+length] in self.words):
					pts += length

		pts /= len(s)
		return (pts ** 2.0) * 0.8

	@utils.cache
	def score(self, text):
		if (self.unidec):
			text = unidecode(text).upper()
		else:
			text = text.upper()
		ngrams_scores = [i * j for i, j in zip(self.ngramWeights, self.scoreNgrams(text))]
		word_score = self.scoreWords(text) * self.wordWeight

		final_score = sum(ngrams_scores) + word_score

		if (self.log):
			print([ngrams_scores, word_score], "Total:", final_score)

		return final_score
