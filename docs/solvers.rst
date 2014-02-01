Solvers
*******

Solvers glue everything we have learned so far together. They will get some keys from a KeyGenerator, apply these keys to the cipher with a Translator and finally score these solutions with a Scorer. They will also take care of printing out progress and optional interactions (during the solving process) from the user.

To date, there are only two Solvers. Since they are so essential for pycrypt's use, we'll go over both of them.

Basic usage
===========

BruteForceSolver
----------------

We'll be trying to solve a `Vigenère cipher <http://en.wikipedia.org/wiki/Vigenere_cipher>`_. First, we will make the actual cipher:

.. code-block:: python

	import pycrypt as pc

	text = "The White-bellied Sea Eagle is a large diurnal bird of prey in the family Accipitridae. A distinctive bird, adults have a white head, breast, under-wing coverts and tail. The upper parts are grey and the black under-wing flight feathers contrast with the white coverts."
	t = pc.VigenereTranslator(key="EGG")
	cipher = t.encode(text)

	print cipher

We will get the encoded output::

	OAX RABOX-UZEEDXW NXT ZTZGX BN T EVKZZ WBPKGVE UDKW JY IMXR DG MCX YVFBGR TXVBKBMMBWVX. T YBLOBGXMBQX UDKW, VWNGML CTOZ T PCBMZ AXVW, UMXTNM, NIWXM-PBIZ VJOXMML VGW OTBG. MAZ NIKXK KTKOL TMX ZMXR VGW OAX WETXD NIWXM-PBIZ YGBZCM YZTMCXKN VHIMKVLM RBMC MAZ PADMX XHOZKMN.

Since the Vigenère cipher key is only 3 characters long, the ``BruteForceSolver`` should suffice:

.. code-block:: python

	s = pc.BruteForceSolver(keyGenerator=pc.CombinationKeyGenerator(length_range=(1, 3)),
		 translator=pc.VigenereTranslator(), scorer=pc.EnglishScorer())
	s.solve(cipher)

The first line sets up our ``BruteForceSolver``. ``CombinationKeyGenerator`` with small ``length_range``, so that we can try out all the keys, obviously ``VigenereTranslator`` as the specified Translator and ``EnglishScorer``.

.. tip::

	You can set the default scorer in the conf.py file

When you'll run this, you should see all of the possible keys with their respective solution previews. In 15 seconds or so, the final output will look like this::

	...
	Score: 0.35820      Key: ZZU      Text: OAS RAWOX-PZEZDXR NXO ZTUGX WN T ZVKUZ WWPKBVE PDKR JY DMXM DG HCX TVFWGR OXVWKB
	Score: 0.36785      Key: ZZV      Text: OAT RAXOX-QZEADXS NXP ZTVGX XN T AVKVZ WXPKCVE QDKS JY EMXN DG ICX UVFXGR PXVXKB
	Score: 0.29618      Key: ZZW      Text: OAU RAYOX-RZEBDXT NXQ ZTWGX YN T BVKWZ WYPKDVE RDKT JY FMXO DG JCX VVFYGR QXVYKB
	Score: 0.33593      Key: ZZX      Text: OAV RAZOX-SZECDXU NXR ZTXGX ZN T CVKXZ WZPKEVE SDKU JY GMXP DG KCX WVFZGR RXVZKB
	Score: 0.41876      Key: ZZY      Text: OAW RAAOX-TZEDDXV NXS ZTYGX AN T DVKYZ WAPKFVE TDKV JY HMXQ DG LCX XVFAGR SXVAKB
	Score: 0.33509      Key: ZZZ      Text: OAX RABOX-UZEEDXW NXT ZTZGX BN T EVKZZ WBPKGVE UDKW JY IMXR DG MCX YVFBGR TXVBKB

	=====Best Solution=====
	Score: 2.89494237918
	Key: EGG
	Text: THE WHITE-BELLIED SEA EAGLE IS A LARGE DIURNAL BIRD OF PREY IN THE FAMILY ACCIPITRIDAE. A DISTINCTIVE BIRD, ADULTS HAVE A WHITE HEAD, BREAST, UNDER-WING COVERTS AND TAIL. THE UPPER PARTS ARE GREY AND THE BLACK UNDER-WING FLIGHT FEATHERS CONTRAST WITH THE WHITE COVERTS.

If we would know, that the key was a meaningful word, we could use for instance some sort of word list KeyGenerator (which, as of now, doesn't exist). 

GeneticSolver
-------------

3 character long keys take about 20 seconds with the ``BruteForceSolver``, but 4 characters would take 26 times that! That is over 8 minutes. To try out all the possible 8 character keys, it would take over 6000 years. That's where the ``GeneticSolver`` comes in. It uses a very basic `genetic algorithm <http://en.wikipedia.org/wiki/Genetic_algorithm>`_. But first, let's make a more complex Vigenère cipher from our sample text:

.. code-block:: python

	t.setKey("SPAMANDEGGS")
	cipher = t.encode(text)

	print cipher

We'll get this::

	ARD JGUPZ-UXSSSDQ RQW ZTZSL SR N KMNBX WPBBMNK NEMW HM WBDL HZ PCX YHTSKL ZOYDIBAYSCND. M ZDLMPUMSVUQ XDKW, HKEKGR TWQX T DOSSR GQWY, UKLHCS, HMPAM-PBUN MNIDDPN TGK AKHY. STA PIILY ZZESE WMX ZYLI ZAC FDZ UEHJU TACQN-RBGN MVHTGF BZTMOLBR PNZPMTLA DSSU STA RABAL MNIDDPN.

Now let's try to solve it:

.. code-block:: python

	s = pc.GeneticSolver(keyGenerator=pc.CombinationKeyGenerator(length_range=(1, 11)),
		 translator=pc.VigenereTranslator(), scorer=pc.EnglishScorer())
	s.solve(cipher)

You *should* see output similar (but maybe very different) to this::

	 1.      Score: 0.74231      Text: HLE ENNWT-VSZLZXR MXP GNANS LY H LHUUE QQWIFUE OZTP OG XWKE OT QXE RONTFS SVSEDI
	 2.      Score: 0.85933      Text: THE QZOSP-KMFLIEX KKZ PJOFE IS U DGQRN LCURNUD HHCM WZ PRES AT SSN NUMILS SIBTYQ
	 3.      Score: 0.93790      Text: THE QZOSP-KMILIEX KKZ PJOIE IS U DGQRN LFURNUD HHCM WC PRES AT SSN NXMILS SIBTYQ
	 4.      Score: 1.02072      Text: THE QZOSV-KMLLIEX KKZ VJOLE IS U DGQXN LIURNUD HHIM WF PRES AT SYN NAMILS SIBZYQ
	 5.      Score: 1.11349      Text: THE QZOSE-BMILIEX KKZ EAOIE IS U DGQGE LFURNUD HHRD WC PRES AT SHE NXMILS SIBIPQ
	 6.      Score: 1.13169      Text: THE QOOSB-KMLLIEX ZKZ BJOLE IS U SGQDN LIURNUS HHOM WF PRES PT SEN NAMILS HIBFYQ
	 7.      Score: 1.36420      Text: THE QZOTE-BMILIEX KKA EAOIE IS U DGRGE LFURNUD HIRD WC PRES AT THE NXMILS SICIPQ
	 8.      Score: 1.36962      Text: THE QZOTE-BHILIEX KKA EAJIE IS U DGRGE GFURNUD HIRD RC PRES AT THE IXMILS SICIPL
	 9.      Score: 1.74856      Text: THE QZITE-BMILIEX KEA EAOIE IS U DARGE LFURNUD BIRD WC PRES AN THE NXMILS SCCIPQ
	10.      Score: 1.88447      Text: THE QZITE-BEILIEX KEA EAGIE IS U DARGE DFURNUD BIRD OC PRES AN THE FXMILS SCCIPI
	11.      Score: 2.20848      Text: THE QZITE-BELLIEX KEA EAGLE IS U DARGE DIURNUD BIRD OF PRES AN THE FAMILS SCCIPI
	12.      Score: 2.31031      Text: THE WZITE-BELLIED KEA EAGLE IS A DARGE DIURNAD BIRD OF PREY AN THE FAMILY SCCIPI
	13.      Score: 2.34455      Text: THE WTITE-BELLIED EEA EAGLE IS A XARGE DIURNAX BIRD OF PREY UN THE FAMILY MCCIPI
	14.      Score: 2.63445      Text: THE QHITE-BELLIEX SEA EAGLE IS U LARGE DIURNUL BIRD OF PRES IN THE FAMILS ACCIPI
	15.      Score: 2.63445      Text: THE QHITE-BELLIEX SEA EAGLE IS U LARGE DIURNUL BIRD OF PRES IN THE FAMILS ACCIPI
	16.      Score: 2.63445      Text: THE QHITE-BELLIEX SEA EAGLE IS U LARGE DIURNUL BIRD OF PRES IN THE FAMILS ACCIPI
	17.      Score: 2.89494      Text: THE WHITE-BELLIED SEA EAGLE IS A LARGE DIURNAL BIRD OF PREY IN THE FAMILY ACCIPI
	18.      Score: 2.89494      Text: THE WHITE-BELLIED SEA EAGLE IS A LARGE DIURNAL BIRD OF PREY IN THE FAMILY ACCIPI

If you'll stop the process with Ctrl-C (you have to be in some sort of interactive shell), you'll see the last evolution::

	18.      Score: 2.89494      Text: THE WHITE-BELLIED SEA EAGLE IS A LARGE DIURNAL BIRD OF PREY IN THE FAMILY ACCIPI
	Evolution interrupted! Setting starting point to continue

	=====Best Solution=====
	Score: 2.89494237918
	Key: ['S', 'P', 'A', 'M', 'A', 'N', 'D', 'E', 'G', 'G', 'S']
	Text: THE WHITE-BELLIED SEA EAGLE IS A LARGE DIURNAL BIRD OF PREY IN THE FAMILY ACCIPITRIDAE. A DISTINCTIVE BIRD, ADULTS HAVE A WHITE HEAD, BREAST, UNDER-WING COVERTS AND TAIL. THE UPPER PARTS ARE GREY AND THE BLACK UNDER-WING FLIGHT FEATHERS CONTRAST WITH THE WHITE COVERTS.

.. warning::

	Right now, it is not unusual for the genetic algorithm to get stuck in a local maxima. It does not happen often, but when it does, just restart the script. It shouldn't happen in the future, as many improvements are planned to the actual algorithm as well as some more tools to help to resolve this problem.

As you can see, the ``GeneticSolver`` can prove to be highly effective. You'll want to use them in most cases, however, if you can try out all the keys in a reasonable time, ``BruteForceSolver`` is a better choice, as the ``GeneticSolver`` can prove unreliable sometimes.

Advanced usage
==============

Let's move on to a more complex case of a cipher, such as a substitution cipher. Again, we'll make the encoded text first:

.. code-block:: python

	t = pc.SubstitutionTranslator()
	t.setKey(dict(zip(pc.alphabet, reversed(pc.alphabet))))
	cipher = t.encode(text)

	print cipher

We set the ``SubstitutionTranslator`` key to a reversed alphabet (which produces a very simple cipher), but we could have chosen any possible unordered alphabet, this is just for illustration. We'll end up with this cipher::

	GSV DSRGV-YVOORVW HVZ VZTOV RH Z OZITV WRFIMZO YRIW LU KIVB RM GSV UZNROB ZXXRKRGIRWZV. Z WRHGRMXGREV YRIW, ZWFOGH SZEV Z DSRGV SVZW, YIVZHG, FMWVI-DRMT XLEVIGH ZMW GZRO. GSV FKKVI KZIGH ZIV TIVB ZMW GSV YOZXP FMWVI-DRMT UORTSG UVZGSVIH XLMGIZHG DRGS GSV DSRGV XLEVIGH.

Now we will attempt to solve it with the ``GeneticSolver``:

.. code-block:: python

	s = pc.GeneticSolver(keyGenerator=pc.SubstitutionKeyGenerator(),
		 translator=pc.SubstitutionTranslator(), scorer=pc.EnglishScorer())
	s.solve(cipher)

Unless you are very lucky, you will see that the substitution cipher is much harder to solve. You might even want to restart a few times. Let's see an example output::

	  1.      Score: 1.04425      Text: END PNTED-KDMMTDV HDZ DZFMD TH Z MZIFD VTRIAZM KTIV CB YIDQ TA END BZSTMQ ZJJTYT
	  2.      Score: 1.78308      Text: THE KHOTE-NECCOEB WEF EFUCE OW F CFAUE BOPAZFC NOAB LV DAEI OZ THE VFQOCI FGGODO
	  3.      Score: 1.98144      Text: THE KHOTE-NECCOEB WES ESUCE OW S CSAUE BOPAZSC NOAB LV DAEI OZ THE VSQOCI SGGODO
	  4.      Score: 2.03995      Text: THE KHOTE-BECCOEN WES ESUCE OW S CSAUE NOPAZSC BOAN LV DAEI OZ THE VSQOCI SGGODO
	  5.      Score: 2.11829      Text: THE KHOTE-BECCOEN WES ESUCE OW S CSAUE NOPARSC BOAN LV DAEI OR THE VSQOCI SGGODO
	  6.      Score: 2.18511      Text: THE KHOTE-BECCOEN WES ESUCE OW S CSRUE NOPRASC BORN LV DREI OA THE VSQOCI SGGODO
	  7.      Score: 2.21979      Text: THE CHOTE-LEJJOEN WES ESBJE OW S JSABE NOPAISJ LOAN VU DAER OI THE USQOJR SGGODO
	  8.      Score: 2.27611      Text: THE KHOTE-BECCOEN WES ESUCE OW S CSRUE NOPRFSC BORN LV IRED OF THE VSQOCD SAAOIO
	  9.      Score: 2.34155      Text: THE WHOTE-QEVVOEB RES ESGVE OR S VSAGE BOIANSV QOAB YC PAED ON THE CSZOVD SUUOPO
	 10.      Score: 2.38612      Text: THE WHITE-QEVVIEB RES ESGVE IR S VSAGE BIOANSV QIAB YK PAED IN THE KSZIVD SUUIPI
	 11.      Score: 2.40644      Text: THE WHOTE-QEVVOEU AES ESGVE OA S VSRGE UOIRNSV QORU YC PRED ON THE CSZOVD SBBOPO
	 12.      Score: 2.46465      Text: THE VHOTE-QERROED FEA EAGRE OF A RASGE DOISNAR QOSD YC PSEB ON THE CAZORB AUUOPO
	 13.      Score: 2.48524      Text: THE WHOTE-QERROED FES ESGRE OF S RSIGE DOAINSR QOID YC PIEB ON THE CSZORB SUUOPO
	 Evolution interrupted! Setting starting point to continue

	=====Best Solution=====
	Score: 2.46465315985
	Key:
	ABCDEFGHIJKLMNOPQRSTUVWXYZ
	KBWVLITFSXPYNZRJMOHGCEDUQA
	Text: THE VHOTE-QERROED FEA EAGRE OF A RASGE DOISNAR QOSD YC PSEB ON THE CAZORB AUUOPOTSODAE. A DOFTONUTOLE QOSD, ADIRTF HALE A VHOTE HEAD, QSEAFT, INDES-VONG UYLESTF AND TAOR. THE IPPES PASTF ASE GSEB AND THE QRAUJ INDES-VONG CROGHT CEATHESF UYNTSAFT VOTH THE VHOTE UYLESTF.

At the end, we have stopped the process with Ctrl-C. If you are using an interactive python shell (e.g. regular command-line python, ipython or IDLE's python shell), you should be able to continue issuing commands.

Interactive mode
----------------

The ability to interrupt the process is very useful, as we can *help* the Solver. You might want to play around with different settings for the algorithm (like population size or the randomness of mutations). But we can have a more direct control. For instance, if we take a look at the last evolution from our last example::

	13.      Score: 2.48524      Text: THE WHOTE-QERROED FES ESGRE OF S RSIGE DOAINSR QOID YC PIEB ON THE CSZORB SUUOPO

We can tell, that the "THE" is probably right. We can then lock it in place, so further evolution doesn't change it.

>>> s.lock("THE")

``GeneticSolver``'s ``lock`` processes the arguments and the just calls its keyGenerator's ``lock`` to add some rules. If no key is set (as an optional argument), it locks according to the key from the last evolution. If we, for example, would know that A translates to Z (which it does), we could call ``SubstitutionKeyGenerator``'s ``lock`` directly:

>>> s.keyGenerator.lock('A', 'Z')

Also now that we have some readable results, we can increase the randomness a bit:

>>> s.keyGenerator.randFunc = lambda x: x ** 3

When the ``SubstitutionKeyGenerator`` calculates how many elements to swap around, it gets a random value between 0 and 1. It is then put through its randFunc. The default is ``lambda x: x ** 6``, so now, it will tend to swap more characters.

.. tip::

	If, for any reason, you want to start the evolution again while keeping the locks, you can do:

	>>> s.setStartingPoint(None)

Now, let's continue the evolution:

>>> s.solve(cipher)

You may have to set up some more locks, but in the end, you should end up with this::

	...
	 17.      Score: 2.89556      Text: THE WHITE-BELLIED SEA EAGLE IS A LARGE DIURNAL BIRD OF PREY IN THE FAMILY ACCIPI
	 Evolution interrupted! Setting starting point to continue

	=====Best Solution=====
	Score: 2.89555799257
	Key:
	ABCDEFGHIJKLMNOPQRSTUVWXYZ
	ZYXWVUTSRQPONMLKJIHGFEDCBA
	Text: THE WHITE-BELLIED SEA EAGLE IS A LARGE DIURNAL BIRD OF PREY IN THE FAMILY ACCIPITRIDAE. A DISTINCTIVE BIRD, ADULTS HAVE A WHITE HEAD, BREAST, UNDER-WING COVERTS AND TAIL. THE UPPER PARTS ARE GREY AND THE BLACK UNDER-WING FLIGHT FEATHERS CONTRAST WITH THE WHITE COVERTS.

As we can see, the correct key is in fact the reversed alphabet.

Making your own Solver
======================

All you have to do is to implement the ``solve`` method. You should be supporting the ``startingPoint`` variable, as it is a useful feature. For printing, there are prepared the ``printer`` and ``lastPrint`` methods. (TODO)

Next steps
==========

We have covered Solvers, which is the last part of pycrypt. You should be now able to use it efficiently.

Next, we will go over some useful external modules, which could come in handy.

If you want more guidelines, you can see example uses on ciphers from real cryptography game (hopefully regularly updated).

Further reading
===============

To see the source code of Solvers, you can refer to the API:

.. seealso::
	
	`Solvers <pycrypt.solvers.html>`_