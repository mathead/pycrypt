"""
Simple Vigenere cipher, example covered in documentation
"""
import pycrypt as pc

text = "The White-bellied Sea Eagle is a large diurnal bird of prey in the family Accipitridae. A distinctive bird, adults have a white head, breast, under-wing coverts and tail. The upper parts are grey and the black under-wing flight feathers contrast with the white coverts."

t = pc.VigenereTranslator(key="SPAMANDEGGS")
cipher = t.encode(text)

print(cipher)

s = pc.GeneticSolver(keyGenerator=pc.CombinationKeyGenerator(length_range=(1, 11)), translator=pc.VigenereTranslator(), scorer=pc.EnglishScorer())
s.solve(cipher)