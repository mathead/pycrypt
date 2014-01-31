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

Since the Vigenère cipher key is only 3 characters long, the ``BruteForceSolver`` should suffice::

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

3 character long keys take about 20 seconds with the ``BruteForceSolver``, but 4 characters would take 26 times that! That is over 8 minutes. To try out all the possible 8 character long keys, it would take over 6000 years. That's where the ``GeneticSolver`` comes in. It uses a very basic `genetic algorithm <http://en.wikipedia.org/wiki/Genetic_algorithm>`_. But first, let's make a more complex Vigenère cipher from our sample text:

.. code-block:: python

	t.setKey("SPAMANDEGGS")
	cipher = t.encode(text)

	print cipher

We'll get this::

	ARD JGUPZ-UXSSSDQ RQW ZTZSL SR N KMNBX WPBBMNK NEMW HM WBDL HZ PCX YHTSKL ZOYDIBAYSCND. M ZDLMPUMSVUQ XDKW, HKEKGR TWQX T DOSSR GQWY, UKLHCS, HMPAM-PBUN MNIDDPN TGK AKHY. STA PIILY ZZESE WMX ZYLI ZAC FDZ UEHJU TACQN-RBGN MVHTGF BZTMOLBR PNZPMTLA DSSU STA RABAL MNIDDPN.


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