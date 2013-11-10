import scorer
from unidecode import unidecode

class LanguageScorer(scorer.Scorer):
	"""Scorer for languages based on N-grams and words"""

	words = None
	minWordLen = 3
	maxWordLen = 10
	log = False
	ngramWeights = None
	wordWeight = 0

	def setIdealNgramFrequencies(self, freqs):
		self.idealNgramFrequencies = freqs
		self.ngramLens = [len(i.keys()[0]) for i in freqs]
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
		d = {}
		for i in range(len(text) - 1 - length):
			if (d.has_key(text[i:i+length])):
				d[text[i:i+length]] += 1.0 / len(text)
			else:
				d[text[i:i+length]] = 1.0 / len(text)

		return d

	def getScoreNgrams(self, text):
		scores = []
		for i, ideal_freq in enumerate(self.idealNgramFrequencies):
			scores.append(0.0)
			if (self.ngramWeights[i]): # 0 is to ignore

				text_freq = self.getNgramFrequencies(text, self.ngramLens[i])

				for ngram in list(set(ideal_freq.keys()) & set(text_freq.keys())): # get only mutual ngrams
					scores[i] += ideal_freq[ngram] * text_freq[ngram] # weird equation, but it works


		return scores
		
	def getScoreWords(self, text):
		if (self.maxWordLen == 0 or self.words == None):
			return 0

		s = self.applyKey(self.ciphered_string, key)
		pts = 0.0
		for length in range(self.minWordLen, self.maxWordLen):
			for pos in range(len(s) - 1 - length):
				if (s[pos:pos+length] in self.words):
					pts += length

		pts /= len(s)
		return (pts ** 2.0) * 0.8

	def getScore(self, text):
		text = unidecode(unicode(text)).upper()
		ngrams_scores = [i * j for i, j in zip(self.ngramWeights, self.getScoreNgrams(text))]
		word_score = self.getScoreWords(text) * self.wordWeight

		final_score = sum(ngrams_scores) + word_score

		if (self.log):
			print([ngrams_scores, word_score], "Total:", final_score)

		return final_score
