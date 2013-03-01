import string
import random
import pprint
import time
import trigrams
import operator
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
	#print sorted(ENGLISH_TRIGRAMS.iteritems(), key=operator.itemgetter(1))

	def DEF_PERM_FUNC(x, iterations=1):
		#i =  x**((((100-iterations)/100.0)+1)*2)
		i =  x**2
		#print iterations, (((100-iterations)/100.0)+1), i
		return i
	#DEF_PERM_FUNC = lambda x: (-1/(x-27.0/26.0))/26.0

	def __init__ (self, frequency=ENGLISH_FREQUENCY, frequencies=None):
		self.baseFrequency = frequency
		self.words = None
		self.maxWordLen = 10
		self.minWordLen = 3
		self.frequencies = frequencies
		if (frequencies == None):
			self.frequencies = [self.baseFrequency, self.ENGLISH_BIGRAMS, self.ENGLISH_TRIGRAMS]

	def loadWords (self, path):
		self.words = set([line.strip().upper() for line in open(path)])
		self.maxWordLen = 10

	def getFrequency (self, s):
		f = dict.fromkeys(self.alphabet, 0.0)
		for c in s:
			if (f.has_key(c)):
				f[c] += 1

		suma = sum(f.values())
		for i in f:
			f[i] /= suma

		return f

	def getFrequencies (self, s, length):
		d = {}
		for i in range(len(s) - 1 - length):
			if (d.has_key(s[i:i+length])):
				d[s[i:i+length]] += 1.0 / len(s)
			else:
				d[s[i:i+length]] = 1.0 / len(s)

		return d

	def applyKey (self, s, key):
		f = ""
		for c in s:
			if (key.has_key(c)):
				f += key[c]
			else:
				f += c
		return f

		# return "".join((key[c] if key.has_key(c) else c) for c in s)

		# return string.translate(s, " " * 65 + "".join(j for i, j in sorted(key.items())) + " " * 165)

	def applyKeyBi (self, s, key):
		try:
			return key[s[0]], key[s[1]]
		except:
			return self.applyKey(s, key)

	def applyKeyTri (self, s, key):
		try:
			return key[s[0]], key[s[1]], key[s[2]]
		except:
			return self.applyKey(s, key)

	def applyReversedKey (self, s, key):
		return self.applyKey(s, dict(zip(key.values(), key.keys())))

	def getReversedKey (self, key):
		return dict(zip(key.values(), key.keys()))

	def generateRandomKey (self):
		shuf = list(self.alphabet)
		random.shuffle(shuf)
		"".join(shuf)
		return dict(zip(self.alphabet, shuf))

	def getScore (self, s, f, key): # zatim jednoduse
		f = self.getFrequency(self.applyKey(s, key))
		return 1 - sum(map(lambda a: abs(a[0] - a[1]) / 2, zip(f.values(), self.baseFrequency.values())))

	def getScoreFreq (self, s, f, key):
		d = {}
		for i, j in key.items():
			d[j] = f[i]
		return 1 - sum(map(lambda a: abs(a[0] - a[1]) / 2, zip(d.values(), self.baseFrequency.values())))

	def getScores (self, s, freqs, key, iterations=0, score_list=False):
		scores = self.getScoreNgrams(s, freqs, key)
		if (score_list):
			scores.append(self.getScoreWords(s, key))
			return scores
		#pprint.pprint(scores)
		#result_score = scores[2]

		result_score = 0
		#if iterations > 80:
		#	result_score = scores[0]
		#if iterations <= 60 and iterations > 40:
		#	result_score = scores[1]
		#if iterations <= 40 and iterations > 20:
		#	result_score = scores[2]
		#if iterations <= 20:
		#	result_score = self.getScoreWords(s, key) * 100
		#result_score = score_list[2]
		result_score = scores[0] / 60 + scores[1] / 2 + scores[2] / 1.5
		#result_score = sum(map(lambda x: (x[0] + 1) * x[1], enumerate(scores))) / sum(range(len(scores)))

		if iterations < 10:
			result_score += self.getScoreWords(s, key) * 10
		return result_score

	def getScoreNgrams (self, s, freqs, key):
		scores = []
		i = 0
		for f in freqs:
			translated_freq = {}
			scores.append(0)

			for ngram, ngram_freq in f.items():
				translated_freq[self.applyKey(ngram, key)] = ngram_freq

			for ngram in list(set(self.frequencies[i].keys()) & set(translated_freq.keys())):
				#if (self.frequencies[i].has_key(ngram)):
				#	base = self.frequencies[i][ngram]
				#else:
				#	#continue
				#	base = 0
				#if (translated_freq.has_key(ngram)):
				#	trans = translated_freq[ngram]
				#else:
				#	#continue
				#	trans = 0

				# if (" " in ngram):
				# 	continue	

				#print (abs(base - trans) / 2), scores[i]
				# if (self.frequencies[i].has_key(ngram)) and (translated_freq.has_key(ngram)):
					#print ngram, self.frequencies[i][ngram], translated_freq[ngram]* len(s), self.frequencies[i][ngram]*translated_freq[ngram]*len(s)
				scores[i] += self.frequencies[i][ngram]*translated_freq[ngram]*len(s)
					# scores[i] += self.frequencies[i][ngram]*translated_freq[ngram]*len(s)
					# scores[i] += freq * translated_freq[basengram] * 100
					# if (len(basengram) > 1):
					# 	print basengram
			i += 1

		# print scores
		#for i in range(len(scores)):
		#	scores[i] = 1 - scores[i]
		return scores


	def getScoreWords (self, s, key):
		if (self.maxWordLen == 0):
			return 0

		s = self.applyKey(s, key)
		pts = 0.0
		for length in range(self.minWordLen, self.maxWordLen):
			for pos in range(len(s) - 1 - length):
				if (s[pos:pos+length] in self.words):
					pts += length
					#if (length >= 5):
					#	print s[pos:pos+length]

		pts /= len(s)
		return (pts ** 2) * 0.8

	def getPermutation (self, d, num):
		d = d.copy()
		for i in range(num):
			a = random.choice(self.alphabet)
			b = random.choice(self.alphabet)
			while b == a:
				b = random.choice(self.alphabet)
			# Substituce:
			#d[a] = b
			# Permutace:
			d[a], d[b] = d[b], d[a]

		return d

	def getAllNearPermutations (self, d):
		d = d.copy()
		ret = []
		for i in range(len(d)):
			for j in range(i + 1, len(d) - 1):
				a = d.copy()
				a[self.alphabet[i]], a[self.alphabet[j]] = a[self.alphabet[j]], a[self.alphabet[i]]
				ret.append(a)

		return a

	def generateKey (self, s, population=10, mutations=10, perm_func=DEF_PERM_FUNC, iterations=900, cur=None, log=False, f=None):
		if (log):
			print "iterations", iterations

		if (f == None):
			f = []
			for i in self.frequencies:
				f.append(self.getFrequencies(s, len(i.keys()[0])))

		if (cur == None): # nasamplovani
			cur = []
			for i in range(population):
				cur.append(self.generateRandomKey())
			cur[0] = dict(zip(self.alphabet, self.alphabet))

		if (iterations == 0): # konec
			return cur

		t = time.time()
		mutants = []
		for c in cur:
			if (iterations > 10):
				for m in range(mutations):
					mutants.append(self.getPermutation(c, int(perm_func(random.random(), iterations) * (len(self.baseFrequency) - 1) + 1)))
			else:
				mutants.extend(self.getAllNearPermutations(c))
				print mutants
		if (log):
			print "mutation: ", -(t - time.time())

		mutants.extend(cur)

		# for m in mutants:
		# 	print m

		t = time.time()
		scores = []
		for m in mutants:
			result_score = self.getScores(s, f, m, score_list=False, iterations = iterations)
			scores.append(result_score)

		#if iterations in [99, 70,30]:
		print sorted(zip(scores, mutants))[-1][0]
		print self.applyKey(s, sorted(zip(scores, mutants))[-1][1])[:180]

		mutants_scored = sorted(zip(scores, mutants))[-population:]
		cur = map(lambda x: x[1], mutants_scored)
		if (log):
			print "scoring: ", -(t - time.time())
			print ""

		return self.generateKey(s, population, mutations, perm_func, iterations - 1, cur, log, f)



lipsum = "The White-bellied Sea Eagle is a large diurnal bird of prey in the family Accipitridae. A distinctive bird, adults have a white head, breast, under-wing coverts and tail. The upper parts are grey and the black under-wing flight feathers contrast with the white coverts."
# Like many raptors, the female is slightly larger than the male, and can measure up to 90 cm (36 in) long with a wingspan of up to 2.2 m (7 ft), and weigh 4.5 kg (10 lb). The call is a loud goose-like honking. Resident from India and Sri Lanka through southeast Asia to Australia on coasts and major waterways, the White-bellied Sea Eagle breeds and hunts near water, and fish form around half of its diet. Opportunistic, it consumes carrion and a wide variety of animals. Although rated of Least Concern globally, it has declined in parts of southeast Asia such as Thailand, and southeastern Australia. Human disturbance to its habitat is the main threat, both from direct human activity near nests which impacts on breeding success, and from removal of suitable trees for nesting. The White-bellied Sea Eagle is revered by indigenous people in many parts of Australia, and is the subject of various folk tales throughout its range."
lipsum = lipsum.upper()
d = Decoder()
d.loadWords("/usr/share/dict/words")
#k = dict(zip(d.alphabet, d.alphabet))

# lipsum = "LIVITCSWPIYVEWHEVSRIQMXLEYVEOIEWHRXEXIPFEMVEWHKVSTYLXZIXLIKIIXPIJVSZEYPERRGERIMWQLMGLMXQERIWGPSRIHMXQEREKIETXMJTPRGEVEKEITREWHEXXLEXXMZITWAWSQWXSWEXTVEPMRXRSJGSTVRIEYVIEXCVMUIMWERGMIWXMJMGCSMWXSJOMIQXLIVIQIVIXQSVSTWHKPEGARCSXRWIEVSWIIBXVIZMXFSJXLIKEGAEWHEPSWYSWIWIEVXLISXLIVXLIRGEPIRQIVIIBGIIHMWYPFLEVHEWHYPSRRFQMXLEPPXLIECCIEVEWGISJKTVWMRLIHYSPHXLIQIMYLXSJXLIMWRIGXQEROIVFVIZEVAEKPIEWHXEAMWYEPPXLMWYRMWXSGSWRMHIVEXMSWMGSTPHLEVHPFKPEZINTCMXIVJSVLMRSCMWMSWVIRCIGXMWYMX"
#random.seed(1)

print lipsum[:100]
print d.getScores(lipsum, [d.getFrequencies(lipsum, 1), d.getFrequencies(lipsum, 2), d.getFrequencies(lipsum, 3)], dict(zip(d.alphabet, d.alphabet)), score_list=True), d.getScores(lipsum, [d.getFrequencies(lipsum, 1), d.getFrequencies(lipsum, 2), d.getFrequencies(lipsum, 3)], dict(zip(d.alphabet, d.alphabet)), score_list=False)
lipsum = d.applyKey(lipsum, d.generateRandomKey())
print d.getScores(lipsum, [d.getFrequencies(lipsum, 1), d.getFrequencies(lipsum, 2), d.getFrequencies(lipsum, 3)], dict(zip(d.alphabet, d.alphabet)), score_list=True), d.getScores(lipsum, [d.getFrequencies(lipsum, 1), d.getFrequencies(lipsum, 2), d.getFrequencies(lipsum, 3)], dict(zip(d.alphabet, d.alphabet)), score_list=False)
print lipsum[:100]

run("d.generateKey(lipsum, iterations=10, mutations=20, population=20, log=False)")
# run("d.generateKey(lipsum, iterations=10, mutations=20, population=20, log=True)")
# for a in b:
# 	print d.getScores(lipsum, [d.getFrequencies(lipsum, 1), d.getFrequencies(lipsum, 2), d.getFrequencies(lipsum, 3)], a, score_list=True), d.getScores(lipsum, [d.getFrequencies(lipsum, 1), d.getFrequencies(lipsum, 2), d.getFrequencies(lipsum, 3)], a, score_list=False)
# 	print d.applyKey(lipsum[:], a)

# m = 0
# mk = None
# for i in range(1000):
# 	k = d.generateRandomKey()
# 	if (d.getScore(lipsum, k) > m):
# 		mk = k
# 		m = d.getScore(lipsum, k)

# print (m)
# print d.applyKey(lipsum[:100], mk)
