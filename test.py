# -*- coding: utf-8 -*-

from unidecode import unidecode
import pycrypt as pc
from cProfile import run

if __name__ ==  '__main__':
    a = pc.ThreadedGeneticSolver(log=True, keyGenerator=pc.SubstitutionKeyGenerator(weighted=pc.CzechFrequencies.monograms))
    text = unidecode(u"Na začátku si musíme vytvořit tabulku substitucí, což je tabulka, která znázorňuje, které písmeno v otevřeném textu se mění na jaké v šifrovém textu. Tabulku můžeme vytvořit libovolným způsobem, ale platí, že zobrazení musí být bijektivní, tedy každé písmeno z otevřeného textu musí mít jedinečný obraz v šifrovém textu. Pokud by se například písmeno „a“ zobrazilo na písmeno „q“ a písmeno „b“ by se také zobrazilo na písmeno „q“, vznikla by nám kolize a při dešifrování bychom nevěděli, zda písmeno „q“ dešifrovat na „a“ nebo na „b“. A naopak: písmeno v otevřeném textu musí mít pouze jeden obraz, nemůžeme písmeno „a“ jednou zašifrovat na „b“ a jindy na „c“. Pak už to nebyla jednoduchá monoalfabetická šifra, ale homofonní šifra nebo některá z polyalfabetických šifer, které při šifrování používají více abeced, například Vigenèrova šifra.")
    a.solve(text=text, iterations=4)
    a.plotLog()

    # text = "In the field of artificial intelligence, a genetic algorithm (GA) is a search heuristic that mimics the process of natural selection. This heuristic (also sometimes called a metaheuristic) is routinely used to generate useful solutions to optimization and search problems. Genetic algorithms belong to the larger class of evolutionary algorithms (EA), which generate solutions to optimization problems using techniques inspired by natural evolution, such as inheritance, mutation, selection, and crossover."
    #
    # t = pc.SubstitutionTranslator()
    # t.setKey(dict(zip(pc.alphabet, reversed(pc.alphabet))))
    # cipher = t.encode(text)
    #
    # s = pc.ThreadedGeneticSolver(scorer=pc.EnglishScorer(), log=True)
    # s.solve(cipher, iterations=6)
    # s.plotLog()