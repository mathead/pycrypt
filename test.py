# -*- coding: utf-8 -*-

from unidecode import unidecode
import pycrypt as pc
from cProfile import run

if __name__ ==  '__main__':
    a = pc.GeneticSolver(log=True)
    text = unidecode(u"Na začátku si musíme vytvořit tabulku substitucí, což je tabulka, která znázorňuje, které písmeno v otevřeném textu se mění na jaké v šifrovém textu. Tabulku můžeme vytvořit libovolným způsobem, ale platí, že zobrazení musí být bijektivní, tedy každé písmeno z otevřeného textu musí mít jedinečný obraz v šifrovém textu. Pokud by se například písmeno „a“ zobrazilo na písmeno „q“ a písmeno „b“ by se také zobrazilo na písmeno „q“, vznikla by nám kolize a při dešifrování bychom nevěděli, zda písmeno „q“ dešifrovat na „a“ nebo na „b“. A naopak: písmeno v otevřeném textu musí mít pouze jeden obraz, nemůžeme písmeno „a“ jednou zašifrovat na „b“ a jindy na „c“. Pak už to nebyla jednoduchá monoalfabetická šifra, ale homofonní šifra nebo některá z polyalfabetických šifer, které při šifrování používají více abeced, například Vigenèrova šifra.")
    a.solve(text=text, iterations=50)
    pc.plot_genetic_log(a.log)

    # text = "The White-bellied Sea Eagle is a large diurnal bird of prey in the family Accipitridae. A distinctive bird, adults have a white head, breast, under-wing coverts and tail. The upper parts are grey and the black under-wing flight feathers contrast with the white coverts."
    #
    # t = pc.SubstitutionTranslator()
    # t.setKey(dict(zip(pc.alphabet, reversed(pc.alphabet))))
    # cipher = t.encode(text)
    #
    # s = pc.ThreadedGeneticSolver(keyGenerator=pc.SubstitutionKeyGenerator(), translator=pc.SubstitutionTranslator(), scorer=pc.EnglishScorer())
    # s.solve(cipher)