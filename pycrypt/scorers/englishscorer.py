import languagescorer
import englishfrequencies as en

class EnglishScorer(languagescorer.LanguageScorer):
	"""English scorer, frequencies got from interwebz"""
	def __init__(self):
		for i in en.bigrams.keys():
			en.bigrams[i] /= 100
		for i in en.trigrams.keys():
			en.trigrams[i] /= 10000.0
		self.setIdealNgramFrequencies([en.monograms, en.bigrams, en.trigrams])
		self.setWeights([10, 100, 1000])