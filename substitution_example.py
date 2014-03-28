"""
Simple substitution cipher, example covered in documentation
"""
import pycrypt as pc

text = "The White-bellied Sea Eagle is a large diurnal bird of prey in the family Accipitridae. A distinctive bird, adults have a white head, breast, under-wing coverts and tail. The upper parts are grey and the black under-wing flight feathers contrast with the white coverts."

t = pc.SubstitutionTranslator()
t.setKey(dict(zip(pc.alphabet, reversed(pc.alphabet))))
cipher = t.encode(text)

s = pc.GeneticSolver(keyGenerator=pc.SubstitutionKeyGenerator(), translator=pc.SubstitutionTranslator(), scorer=pc.EnglishScorer())
s.solve(cipher)