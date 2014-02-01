KeyGenerators
*************

KeyGenerators handle generating keys (that was unexpected) for specific translators. They are intended to be used with Solvers, supplementing keys which the Solvers will then try out and process. They can implement generating all keys (for brute force solving), mutating a key (for genetic algorithms), or anything you would need for a specific Solver.

Basic usage
===========

Most of pycrypt's KeyGenerators have a method ``getAllKeys``, which usually returns a python generator:

.. code-block:: python

	>>> import pycrypt as pc
	>>> import itertools

	>>> kg = pc.CombinationKeyGenerator()
	>>> for i in itertools.islice(kg.getAllKeys(), 30):
	>>> 	print i
	('A',)
	('B',)
	('C',)
	('D',)
	('E',)
	('F',)
	('G',)
	('H',)
	('I',)
	('J',)
	('K',)
	('L',)
	('M',)
	('N',)
	('O',)
	('P',)
	('Q',)
	('R',)
	('S',)
	('T',)
	('U',)
	('V',)
	('W',)
	('X',)
	('Y',)
	('Z',)
	('A', 'A')
	('A', 'B')
	('A', 'C')
	('A', 'D')

.. tip::

	``itertools`` is a great python module for working with iterators (generators in this case). It is really handy and has many different uses. You can see the docs `here <http://docs.python.org/2/library/itertools.html>`_.

Here we use ``itertools.islice`` to look at the first 30 results that our ``CombinationKeyGenerator`` provides. As you might expect, it returns every possible combination of letters. Usually, you can also set some rules for the keys generated:

.. code-block:: python

	>>> kg.length_range = (3, 10)
	>>> for i in itertools.islice(kg.getAllKeys(), 5):
	>>> 	print i
	('A', 'A', 'A')
	('A', 'A', 'B')
	('A', 'A', 'C')
	('A', 'A', 'D')
	('A', 'A', 'E')


You can use ``getRandomKey`` to ... well, guess:

.. code-block:: python

	>>> print kg.getRandomKey()
	('Y', 'Q', 'L', 'U', 'Q')
	>>> print kg.getRandomKey()
	('C', 'H', 'M', 'I')
	>>> print kg.getRandomKey()
	('Z', 'C', 'W', 'M', 'F', 'N', 'J', 'C', 'D')
	>>> print kg.getRandomKey()
	('C', 'M', 'Y')

Notice, how the rule we set before (length_range) also applies to this (and all other) method.

Now let's take a look at ``mutateKey``, which is mainly used by the ``GeneticSolver``. ``mutateKey`` returns a similar key based on the random number generator. The entropy can be changed with the rand_func lambda function passed as an optional argument:

.. code-block:: python

	>>> kg.mutateKey("HELLO")
	('H', 'E', 'L', 'L', 'J', 'Z')
	>>> kg.mutateKey("HELLO")
	('H', 'E', 'L', 'P', 'O')
	>>> kg.mutateKey("HELLO")
	('H', 'E', 'L', 'L', 'O', 'M')
	>>> kg.mutateKey("HELLO")
	('H', 'N', 'L', 'L', 'O')
	>>> kg.mutateKey("HELLO")
	('H', 'E', 'L', 'L', 'L')

Making your own KeyGenerator
============================

If you're trying to solve a simpler cipher and all of the possible keys can be tried out in a reasonable time, you can implement only the ``getAllKeys`` method. It is preferred to return a generator, as its lazy evaluation uses almost no memory. For the more complicated ciphers (like the substitution cipher), you should implement ``getRandomKey`` and ``mutateKey``.

.. tip::

	It's great to make some applicable rules to the KeyGenerator. You can then change them interactively during the actual cipher solving and help the solving process head the right way.

Further reading
===============

To check out all KeyGenerators, see the API:

.. seealso::
	
	`KeyGenerators <pycrypt.keygenerators.html>`_
