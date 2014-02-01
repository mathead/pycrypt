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

If we knew, that the key was a meaningful word, we could have used for instance some sort of word list KeyGenerator (which, as of now, doesn't exist). 

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

	s = pc.GeneticSolver(keyGenerator=pc.CombinationKeyGenerator(length_range=(1, 11)), translator=pc.VigenereTranslator(), scorer=pc.EnglishScorer())
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

	Right now, it is not unusual for the GA algorithm to get stuck in a local maxima. It does not happen often, but when it does, just restart the script. It shouldn't happen in the future, as many improvements are planned to the actual algorithm as well as some more tools to help to resolve this problem.

As you can see, the ``GeneticSolver`` can prove to be highly effective. You'll want to use them in most cases, however, if you can try out all the keys in a reasonable time, ``BruteForceSolver`` is a better choice, as the ``GeneticSolver`` can prove unreliable sometimes.

Advanced usage
==============

Interactive mode
----------------

yoyoyo

Substitution cipher example
---------------------------

yoyoyyo

Further reading
===============

To check out all more Solvers, check out the API:

.. seealso::
	
	`Solvers <pycrypt.solvers.html>`_