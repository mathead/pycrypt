"""
Simple substitution cipher, example covered in documentation
"""
import pycrypt as pc

#text = "The White-bellied Sea Eagle is a large diurnal bird of prey in the family Accipitridae. A distinctive bird, adults have a white head, breast, under-wing coverts and tail. The upper parts are grey and the black under-wing flight feathers contrast with the white coverts."
text = """
RBLVR 
SAPZC 
OP 
APWWCN 
GBAUTEVFCN 
ZBSWAXVWRB 
NOAWTLGKFD 
DAVFDC 
QT 
WTFRP 
NWCZGBUVWBNW 
GKOMCAXRTDB 
ZTZVGBUP 
ZVUP 
UKRAVFGVR 
DLPUGV 
OTNWB 
EABGNRP 
FVJTACQ 
FVNTLGBC 
DBSGBWC 
SACDTDB 
ZVNOTGP 
WUTDB 
GVFRC 
ZPR 
QV 
GPZVN 
GP 
RBGTF 
UKLCNWTGTDB 
RBSC
""".replace("\n", "")

#t = pc.SubstitutionTranslator()
#t.setKey(dict(zip(pc.alphabet, reversed(pc.alphabet))))
#cipher = t.encode(text)

# text = "Fcenian bqcbirq wr ebmhziuefgv"
# s = pc.BruteForceSolver(keyGenerator=pc.NumberKeyGenerator(), translator=pc.CaesarTranslator())
# s.solve(text)

text = """Tx aooaymtduisioao eznrdy
eioy unjmAsrla pnkeuatii
coi onvmpvcunzao lxcsinc
ezrvna ai anmhso mle yjtm
snj eoa jo ohuiePmnva hro
oo padh cnsc d eOniatu o
artmvsntmnoaidmunvrpn ooe
nvdkzte"""

text = "Avk jvk? Jl at elsip? Kvieu nv at, olzmu iartj dt tsrvony. Chale jilm jln nvsiva, cpm bych chale bya."

text = "rtwqc uvaqdwcuvb ub qahlazc qa udetaiqchchl qeoa ubuv vtc ubuv qeoa vtchbv hvftc dup mbiqa vtc"

text = "vrdlgvivhmghbqegdbtqpwemmfqwfxkjhfvuwekcvlinhxqpwjxfphuwvqukinxhkwagvwwuifqqehukavgpculatrhgeqtdbqezccsaqirlfgogzumuhvkqmrrbthjwmmqymtrdcf"

text = "NJSTEUDMARLAMJUAONVSPIALMATRAELDTPTESJESETPMRSIYAPRDCJNOESMAJEASREDLTIASPLTJMPONIOEMVSTAEVDEADJUEVAT"

text = "OJBDHMXJBDHBUFKHXDLWLWIDCAEPGRGJNGAQPCT"

text = "IKDMPTLTXDKXMXMXSVQJMWHFVDXJQVVDXLJNQIQHVQDVDXWHFHKPZPOHQNGJQZLG"

text = "FOKJXTHSJHIUTSLHAYROKONYIUMKXYMUHEUTXSHYOVWYGHIASIXOKGWMDOKIYGYHYEXYFSHYIOISRNYXEAYXNYNULUXJ00HIOXAUWYIOHMMYIGJOXFUGKOASHIYHIOTSYLYKIGOHKGSNKOVYMUHOJGUXNSWSMKIYGYEXYNUTXYHFGSWISHOJWYIWSHLUOFHUNYROEPSNULKDFGYXWROESWUHISUWSHLUKIYGYTHSADLJHISLAFOHLYXNSHSPGYMSNJLYROXSLJOGHSTSEOXFOWSNJLMJEYHFGOIOADGUESIXOGOKLSN"

text = "CNX QWFBEW QAJGVF YKSQA VXG EGME OMA XZTWWQUB"

text = "ABCACDBEFCGEHIJKEFIHELIKBCDAMNOIDEFPKPKCDPJP"

text = "AOGPHCIAHDJQBEKLHIOQHLBREEABKLBGJLCJSHKRBOCJPMEUJNQBIMOSBCOAHGJIOQHLBROKFJLSBCOKNMLONOKSHKRBTUJKRBGJPAOQMBQBIMOSBCOAHGJPCJKLJQOPJKOL"

s = pc.ThreadedGeneticSolver(keyGenerator=pc.SubstitutionKeyGenerator(), translator=pc.SubstitutionTranslator())
#s = pc.ThreadedGeneticSolver(keyGenerator=pc.CombinationKeyGenerator(length_range=(1, 5)), translator=pc.VigenereTranslator())

#s.setStartingPoint(dict(zip(
#    "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
#    "ROUHGCNBQXYLJSMAFKDEVITZWP")))


#s.lock("MESTOKLIZETECKAVYLUSTENEHOGD")
# s.keyGenerator.lock("A", "P")
s.solve(text)
