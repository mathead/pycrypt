import pycrypt as pc

t = [
    "SDTVYDROPEIJ",
    "JECDTSTDEMOD",
    "SNEPUESLDVTS",
    "VRRLDDEEKODE",
    "ITISJETUNNEO",
    "CMYIYDYETSLD",
    "PRDTTSCSCMPS",
    "NEILUMSDIAUE",
    "OSLOERTSNCPT",
    "EJESODELTYEI",
    "SDSEEEDRVRES",
    "NTUSPTSEDEVD",
]

def rot(l):
    return list(zip(*l[::-1]))

class GrilleTranslator(pc.Translator):
    def translate(self, cipher):
        res = ""
        # 01
        # 23
        quadrant_size = len(cipher)//2
        key = [self.key[i:i+quadrant_size] for i in range(quadrant_size)]
        keys = [key, rot(key), rot(rot(rot(key))), rot(rot(key))]
        for r in range(4):
            for i, l in enumerate(cipher):
                for j, c in enumerate(l):
                    quadrant = 2 * (i >= quadrant_size) + (j >= quadrant_size)
                    if keys[quadrant][i%6][j%6] == (quadrant - r) % 4:
                        res += c
        return res

s = pc.ThreadedGeneticSolver(
    keyGenerator=pc.CombinationKeyGenerator(alphabet=list(range(4)), length_range=((len(t)/2)**2,(len(t)/2)**2)),
    translator=GrilleTranslator(),
    crossover=False,
)
s.solve(t)
