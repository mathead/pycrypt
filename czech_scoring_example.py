# -*- coding: utf-8 -*-

import pycrypt as pc
from unidecode import unidecode

a = pc.CzechScorer()
a.log = True
b = pc.CaesarTranslator()
text = unidecode(u"Na začátku si musíme vytvořit tabulku substitucí, což je tabulka, která znázorňuje, které písmeno v otevřeném textu se mění na jaké v šifrovém textu. Tabulku můžeme vytvořit libovolným způsobem, ale platí, že zobrazení musí být bijektivní, tedy každé písmeno z otevřeného textu musí mít jedinečný obraz v šifrovém textu. Pokud by se například písmeno „a“ zobrazilo na písmeno „q“ a písmeno „b“ by se také zobrazilo na písmeno „q“, vznikla by nám kolize a při dešifrování bychom nevěděli, zda písmeno „q“ dešifrovat na „a“ nebo na „b“. A naopak: písmeno v otevřeném textu musí mít pouze jeden obraz, nemůžeme písmeno „a“ jednou zašifrovat na „b“ a jindy na „c“. Pak už to nebyla jednoduchá monoalfabetická šifra, ale homofonní šifra nebo některá z polyalfabetických šifer, které při šifrování používají více abeced, například Vigenèrova šifra.")
for i in range(26):
	b.setKey(i + 3)
	ctext = b.translate(text)
	print(ctext)
	a.score(ctext)
	print("\n\n\n")