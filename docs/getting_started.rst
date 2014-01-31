Getting started
***************

Getting pycrypt
===============

Right now, the only way to get pycrypt is to clone it from github `here <https://github.com/PrehistoricTeam/pycrypt/>`_.
You can clone it with:

.. code-block:: bash

	$ git clone https://github.com/PrehistoricTeam/pycrypt.git

Prerequisites
=============

Pycrypt was developed on Python 2.7.5, but should work fine on previous versions as well.

If you don’t have pip (you should), run this first:

.. code-block:: bash

	$ curl https://raw.github.com/pypa/pip/master/contrib/get-pip.py | python


For graphical capabilities, NumPy and pyplot are required. You can get these modules with pip:

.. code-block:: bash
	
	$ pip install numpy
	$ pip install pyplot

Optional, but recommended modules are unidecode and ipython console for interactive use:

.. code-block:: bash

	$ pip install unidecode
	$ pip install ipython

Running tests
=============

Pycrypt has some unit tests, you can run them in shell, while in the root directory of pycrypt, with:

.. code-block:: bash

	$ python -m unittest discover

First script
============

To start solving a basic `substitution cipher <http://en.wikipedia.org/wiki/Substitution_cipher>`_, try out this code:

.. code-block:: python
	
	import pycrypt as pc

	cipher = "ERU NRIEU-GUFFIUH YUA UAMFU IY A FALMU HISLTAF GILH QX CLUB IT ERU XAWIFB APPICIELIHAU. A HIYEITPEIOU GILH, AHSFEY RAOU A NRIEU RUAH, GLUAYE, STHUL-NITM PQOULEY ATH EAIF. ERU SCCUL CALEY ALU MLUB ATH ERU GFAPZ STHUL-NITM XFIMRE XUAERULY PQTELAYE NIER ERU NRIEU PQOULEY."
	solver = pc.GeneticSolver(scorer=pc.EnglishScorer())

	solver.solve(cipher)

Put it in a file (e.g. first_test.py) in the root directory and run it. You'll see some output and after some time, you *should* see the result close to::

	The White-bellied Sea Eagle is a large diurnal bird of prey in the family Accipitridae. A distinctive bird, adults have a white head, breast, under-wing coverts and tail. The upper parts are grey and the black under-wing flight feathers contrast with the white coverts.
	