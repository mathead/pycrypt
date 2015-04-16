.. pycrypt documentation master file, created by
   sphinx-quickstart on Tue Jan 14 12:36:55 2014.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to pycrypt's documentation!
===================================

Pycrypt is a python suite for solving ciphers at (mostly Czech) cryptography games.

Changelog
---------

v0.2 - Apr 16, 2015
^^^^^^^^^^^^^^^^^^^

* ``ThreadedGeneticSolver``, a new solver implementing the island model
* ``crossovers`` module with some crossover and selection strategies
* Weighted mutations based on letter frequencies
* Plotting the progress of genetic solvers
* Cached scoring for faster evolution
* Pycrypt can now be installed directly from github with pip
* Other fixes, tweaking and improvements

There's a longer post about v0.2 `here <v2news.html>`_

v0.1 - Mar 18, 2014
^^^^^^^^^^^^^^^^^^^

Initial release.

Contents:
---------

.. toctree::
   :maxdepth: 3

   introduction
   getting_started
   structure
   translators
   keygenerators
   scorers
   solvers
   v2news
   pycrypt



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

