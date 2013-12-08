# -*- coding: utf-8 -*-

from unidecode import unidecode
import pycrypt as pc
from cProfile import run

# a = pc.BruteForceSolver()
# b = pc.CaesarTranslator(key=6)
# print a.findBestKey(text=b.translate("Ahoj mami, jak se mas? Ja se mam dobre!"), return_all_keys=True)

a = pc.GeneticSolver()
# text = unidecode(u"Na začátku si musíme vytvořit tabulku substitucí, což je tabulka, která znázorňuje, které písmeno v otevřeném textu se mění na jaké v šifrovém textu. Tabulku můžeme vytvořit libovolným způsobem, ale platí, že zobrazení musí být bijektivní, tedy každé písmeno z otevřeného textu musí mít jedinečný obraz v šifrovém textu. Pokud by se například písmeno „a“ zobrazilo na písmeno „q“ a písmeno „b“ by se také zobrazilo na písmeno „q“, vznikla by nám kolize a při dešifrování bychom nevěděli, zda písmeno „q“ dešifrovat na „a“ nebo na „b“. A naopak: písmeno v otevřeném textu musí mít pouze jeden obraz, nemůžeme písmeno „a“ jednou zašifrovat na „b“ a jindy na „c“. Pak už to nebyla jednoduchá monoalfabetická šifra, ale homofonní šifra nebo některá z polyalfabetických šifer, které při šifrování používají více abeced, například Vigenèrova šifra.")
text = 'MZ AZXZGPF HR NFHRNV EBGELIRG GZYFOPF HFYHGRGFXR, XLA QV GZYFOPZ, PGVIZ AMZALIMFQV, PGVIV KRHNVML E LGVEIVMVN GVCGF HV NVMR MZ QZPV E HRUILEVN GVCGF. GZYFOPF NFAVNV EBGELIRG ORYLELOMBN AKFHLYVN, ZOV KOZGR, AV ALYIZAVMR NFHR YBG YRQVPGREMR, GVWB PZAWV KRHNVML A LGVEIVMVSL GVCGF NFHR NRG QVWRMVXMB LYIZA E HRUILEVN GVCGF. KLPFW YB HV MZKIRPOZW KRHNVML ,,Z" ALYIZAROL MZ KRHNVML ,,J" Z KRHNVML ,,Y" YB HV GZPV ALYIZAROL MZ KRHNVML ,,J", EAMRPOZ YB MZN PLORAV Z KIR WVHRUILEZMR YBXSLN MVEVWVOR, AWZ KRHNVML ,,J" WVHRUILEZG MZ ,,Z" MVYL MZ ,,Y". Z MZLKZP: KRHNVML E LGVEIVMVN GVCGF NFHR NRG KLFAV QVWVM LYIZA, MVNFAVNV KRHNVML ,,Z" QVWMLF AZHRUILEZG MZ ,,Y" Z QRMWB MZ ,,X". KZP FA GL MVYBOZ QVWMLWFXSZ NLMLZOUZYVGRXPZ HRUIZ, ZOV SLNLULMMR HRUIZ MVYL MVPGVIZ A KLOBZOUZYVGRXPBXS HRUVI, PGVIV KIR HRUILEZMR KLFAREZQR ERXV ZYVXVW, MZKIRPOZW ERTVMVILEZ HRUIZ.'
# a.findBestKey(text=text)
run("a.findBestKey(text=text, iterations=5)")