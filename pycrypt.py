import string
import random
import pprint
import time
import trigrams
import operator
import pyevolve
from pyevolve import G1DList
from pyevolve import GSimpleGA
from pyevolve import Selectors, Mutators
from cProfile import run

class Decoder ():
	alphabet = string.uppercase
	ENGLISH_FREQUENCY = dict(zip(alphabet,map(lambda i: i / 100, [8.167,1.492,2.782,4.253,12.702,2.228,2.015,6.094,6.966,0.153,0.772,4.025,2.406,6.749,7.50,1.92,0.095,5.987,6.327,9.056,2.758,0.978,2.360,0.150,1.974,0.074])))
	ENGLISH_BIGRAMS = {"TH":1.52,"EN":0.55,"NG":0.18,"HE":1.28,"ED":0.53,"OF":0.16,"IN":0.94,"TO":0.52,"AL":0.09,"ER":0.94,"IT":0.50,"DE":0.09,"AN":0.82,"OU":0.50,"SE":0.08,"RE":0.68,"EA":0.47,"LE":0.08,"ND":0.63,"HI":0.46,"SA":0.06,"AT":0.59,"IS":0.46,"SI":0.05,"ON":0.57,"OR":0.43,"AR":0.04,"NT":0.56,"TI":0.34,"VE":0.04,"HA":0.56,"AS":0.33,"RA":0.04,"ES":0.56,"TE":0.27,"LD":0.02,"ST":0.55,"ET":0.19,"UR":0.02}
	ENGLISH_TRIGRAMS = trigrams.ENGLISH_TRIGRAMS
	for i in ENGLISH_BIGRAMS.keys():
		ENGLISH_BIGRAMS[i] /= 100
	for i in ENGLISH_TRIGRAMS.keys():
		ENGLISH_TRIGRAMS[i] /= 10000.0

	def __init__(self, ciphered_string, ideal_frequencies = [ENGLISH_FREQUENCY, ENGLISH_BIGRAMS, ENGLISH_TRIGRAMS]):
		self.words = None
		self.maxWordLen = 10
		self.minWordLen = 3
		self.ideal_frequencies = ideal_frequencies
		self.ciphered_string = ciphered_string

	def loadWords(self, path):
		self.words = set([line.strip().upper() for line in open(path)])
		self.maxWordLen = 10

	def applyKey(self, s, key):
		f = ""
		for c in s:
			if (key.has_key(c)):
				f += key[c]
			else:
				f += c
		return f

	def getFrequencies(self, s, length):
		d = {}
		for i in range(len(s) - 1 - length):
			if (d.has_key(s[i:i+length])):
				d[s[i:i+length]] += 1.0 / len(s)
			else:
				d[s[i:i+length]] = 1.0 / len(s)

		return d

	def applyReversedKey(self, s, key):
		return self.applyKey(s, dict(zip(key.values(), key.keys())))

	def getReversedKey(self, key):
		return dict(zip(key.values(), key.keys()))

	def generateRandomKey(self):
		shuf = list(self.alphabet)
		random.shuffle(shuf)
		"".join(shuf)
		return dict(zip(self.alphabet, shuf))

	def getScoreFreq(self, s, f, key):
		d = {}
		for i, j in key.items():
			d[j] = f[i]
		return 1 - sum(map(lambda a: abs(a[0] - a[1]) / 2, zip(d.values(), self.baseFrequency.values())))

	def getScoresGlist(self, glist, log=False):
		return self.getScores(self.glistToKey(glist), log)

	def getScores(self, key, log=False):
		scores = self.getScoreNgrams(key)

		result_score = 0
		# displace_index = 0
		# for letter in d.alphabet:
		# 	letter_count = 0
		# 	for key_letter in key.values():
		# 		if letter == key_letter:
		# 			letter_count += 1
		# 	if letter_count > 1:
		# 		displace_index += letter_count
		# displace_index = 26 - displace_index
		score_words = 0 #self.getScoreWords(key)
		result_score = scores[0]/200 + scores[1]/2 + scores[2] / 1.5# + displace_index / 26.0
		#result_score += score_words / 4

		if log == True:
			print scores[0]/200, scores[1]/2, scores[2] / 1.5,# displace_index / 26.0, score_words / 4
			print result_score

		return result_score

	def glistToKey(self, glist):
		ret = []
		for i in glist:
			ret.append(str(unichr(i)))
		return dict(zip(d.alphabet, ret))

	def getScoreNgrams(self, key):
		scores = []
		freqs = [self.getFrequencies(self.ciphered_string, i) for i in range(1, 4)]
		for i, f in enumerate(freqs):
			translated_freq = {}
			scores.append(0)

			for ngram, ngram_freq in f.items():
				translated_freq[self.applyKey(ngram, key)] = ngram_freq

			for ngram in list(set(self.ideal_frequencies[i].keys()) & set(translated_freq.keys())):
				scores[i] += self.ideal_frequencies[i][ngram]*translated_freq[ngram]*len(self.ciphered_string)

		return scores

	def getScoreWords(self, key):
		if (self.maxWordLen == 0):
			return 0

		s = self.applyKey(self.ciphered_string, key)
		pts = 0.0
		for length in range(self.minWordLen, self.maxWordLen):
			for pos in range(len(s) - 1 - length):
				if (s[pos:pos+length] in self.words):
					pts += length

		pts /= len(s)
		return (pts ** 2) * 0.8
		
lipsum = "The White-bellied Sea Eagle is a large diurnal bird of prey in the family Accipitridae. A distinctive bird, adults have a white head, breast, under-wing coverts and tail. The upper parts are grey and the black under-wing flight feathers contrast with the white coverts."
#The upper parts are grey and the black under-wing flight feathers contrast with the white coverts. Like many raptors, the female is slightly larger than the male, and can measure up to 90 cm (36 in) long with a wingspan of up to 2.2 m (7 ft), and weigh 4.5 kg (10 lb). The call is a loud goose-like honking. Resident from India and Sri Lanka through southeast Asia to Australia on coasts and major waterways, the White-bellied Sea Eagle breeds and hunts near water, and fish form around half of its diet. Opportunistic, it consumes carrion and a wide variety of animals. Although rated of Least Concern globally, it has declined in parts of southeast Asia such as Thailand, and southeastern Australia. Human disturbance to its habitat is the main threat, both from direct human activity near nests which impacts on breeding success, and from removal of suitable trees for nesting. The White-bellied Sea Eagle is revered by indigenous people in many parts of Australia, and is the subject of various folk tales throughout its range."

# lipsum = "hereuponlegrandarosewithagraveandstatelyairandbroughtmethebeetlefromaglasscaseinwhichitwasencloseditwasabeautifulscarabaeusandatthattimeunknowntonaturalistsofcourseagreatprizeinascientificpointofviewthereweretworoundblackspotsnearoneextremityofthebackandalongoneneartheotherthescaleswereexceedinglyhardandglossywithalltheappearanceofburnishedgoldtheweightoftheinsectwasveryremarkableandtakingallthingsintoconsiderationicouldhardlyblamejupiterforhisopinionrespectingit"
#random.seed(1)

lipsum = lipsum.upper()
d = Decoder(lipsum)
d.loadWords("/usr/share/dict/words")

d.getScores(dict(zip(d.alphabet, d.alphabet)), log=True)
print lipsum[:100]

def callback(ga):
	# print sorted(ga.bestIndividual())
	if not ga.getCurrentGeneration() % 10:
		result_genome = ga.bestIndividual()
		d.getScoresGlist(result_genome, log=True)
		b = d.glistToKey(result_genome)
		print d.applyKey(d.ciphered_string, b)
	return False

def G1DListPermInitializator(genome, **args):
	genome.clearList()
	a = range(genome.getListSize())
	random.shuffle(a)
	for i in a:
		genome.append(i + 65)


genome = G1DList.G1DList(26)
genome.setParams(rangemin=65, rangemax=90)
genome.initializator.set(G1DListPermInitializator)
genome.evaluator.set(d.getScoresGlist)
ga = GSimpleGA.GSimpleGA(genome)
# ga.selector.set(Selectors.GTournamentSelector)

# for i in range(10):
ga.setCrossoverRate(0)
ga.setMutationRate(0.5)
ga.stepCallback.set(callback)

# ga.setPopulationSize(1000)
# ga.setGenerations(1)
# ga.evolve(freq_stats=10)
#
ga.setPopulationSize(40)
ga.setGenerations(200)

sqlite_adapter = pyevolve.DBAdapters.DBSQLite(identify="ex1")
ga.setDBAdapter(sqlite_adapter)

# run("ga.evolve(freq_stats=30)")
ga.evolve(freq_stats=10)

result_genome = ga.bestIndividual()
print d.getScoresGlist(result_genome, log=True)
b = d.glistToKey(result_genome)
print d.applyKey(d.ciphered_string, b)
