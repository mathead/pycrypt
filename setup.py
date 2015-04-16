from setuptools import setup

setup(
    name='pycrypt',
    version='0.2',
    author='Matej Hlavacek',
    author_email='hlavacek.matej@gmail.com',
    packages=['pycrypt'],
    license='LICENSE.txt',
    description='Pycrypt is a python suite for solving ciphers at (mostly Czech) cryptography games.',
    long_description=open('README.txt').read(),
    install_requires=[
	"mock",
    "numpy",
    "matplotlib",
	"unidecode",
    "pathos",
    ],
)