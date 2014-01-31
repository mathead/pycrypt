Scorers
*******

Scorers are used by Solvers to see how good a solution is. It can be anything like scoring a Sudoku grid, but usually you'll be using them to score similarity to some language. Pycrypt comes with a Scorer for English and Czech.

Basic usage
===========

Let's see our EnglishScorer in action!

.. code-block:: python

	>>> import pycrypt as pc

	>>> s = pc.EnglishScorer()

	>>> s.score("asdsdghuioz")
	0.5275818181818182

	>>> s.score("Hello World")
	1.0342818181818183

As you can see, the jumbled text scored a half of what the English text did. You might expect a bit larger difference, but this example uses just too short text. There is no normalization of the score, so you could see scores around 1 just as well as scores over 5. Usually, jumbled text scores only a small fraction.

Making your own Scorer
======================

Just extend ``Scorer``'s ``score`` method and you're good to go!

If you want a ``LanguageScorer``, you'll need some frequency statistics, but first, let's look at the ``CzechScorer`` implementation:

.. literalinclude:: ../pycrypt/scorers/czechscorer.py

As you can see, all you have to do is call the ``setIdealNgramFrequencies`` method to load frequency dictionaries. The ``setWeights`` just multiplies the score got from their respective n-gram frequencies (pentagrams are more relevant than monograms and pentagrams usually score much lower because of their limited dictionaries).

The frequency dictionaries are just python ``dict`` s, which have the n-grams as a key and their probability distribution as a value. The values, if all possible keys are referenced, should sum up to 1. The Czech data is generated from `here <http://ufal.mff.cuni.cz/~hajic/courses/npfl067/stats/czech.html>`_. There are only Czech and English statistics to date, but more languages are to come. Should you want to process them, you can use the ngram_converter.py script, which comes with pycrypt.

Keep in mind, that a good Scorer should not only give good score to correct results and bad score to incorrect. It should also give half the score (or log half or something) to half correct results. This is essential, when using the genetic algorithms (and several others), to let the algorithm know, that it is on the right track. You should avoid making too big local maxima as well.

Further reading
===============
To check out Scorers' source, check out the API:

.. seealso::
	
	`Scorers <pycrypt.scorers.html>`_

