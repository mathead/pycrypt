import pycrypt as pc


class MorbitTranslator(pc.Translator):
    def __init__(self, key="ABCDEFGHI"):
        self.setKey(key)

    def setKey(self, key):
        table = ["..", ".-", ". ", "-.", "--", "- ", " .", " -", "  "]
        self.key = list(zip(*sorted(zip(key, table))))[1]

    def translate(self, cipher):
        result = ""
        for c in cipher:
            if c in "123456789":
                result += self.key[int(c)-1]
            else:
                result += c
        return pc.MorseCodeTranslator().translate(result)

text = """35675245125185765425795215325965325465715975435115725785695

27583576581538511526512591533516574538511592594581584576547

51253957856754452259453457957456152852351157752952351152453

857251352259658259258153251754854159759354458259857453952758"""


s = pc.BruteForceSolver(keyGenerator=pc.PermutationKeyGenerator(sequence='ABCDEFGHI'), translator=MorbitTranslator())

s.solve(text)
