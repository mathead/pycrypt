import pycrypt as pc

t = [
"quitegnoitapotitlsurbemiooam",
"conditamvmetaroisiurieamlegi",
"busquetcmoeibusdeistegrocond",
"ereprratquisuscuminterrellaa",
"dsuescereviderebnonpossequip",
"peefferaeimilvtiaantmosmitng",
"andumeerocempopulamaraorumde",
"sustudineratasianumadinfzmum",
]

class BarTranslator(pc.Translator):
    """Basic substitution, default key reversed alphabet"""
    def translate(self, cipher):
        result = []
        for l in cipher:
            n = ""
            for k in self.key:
                n += l[k]
            result.append(n)
        return "\n".join(result)

s = pc.ThreadedGeneticSolver(keyGenerator=pc.PermutationKeyGenerator(sequence=list(range(28))), translator=BarTranslator(), crossover=False)
s.solve(t)
