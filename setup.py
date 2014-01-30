from distutils.core import setup

setup(
    name='pycrypt',
    version='0.1',
    author='Matej Hlavacek',
    author_email='hlavacek.matej@gmail.com',
    packages=['pycrypt'],
    license='LICENSE.txt',
    description='Pycrypt is a python suite for solving ciphers at (mostly Czech) cryptography games.',
    long_description=open('README.txt').read(),
    install_requires=[
        "numpy",
        "pyplot",
    ],
)