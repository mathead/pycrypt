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

As you can see, jumbled text scored a half of what English text did. You might expect a bit larger difference, but this example uses just too short text. There is no normalization of the score, so you could see scores around 1 just as well as scores over 5. Usually, jumbled text scores only a small fraction.