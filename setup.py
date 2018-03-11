import os
from setuptools import setup, find_packages
from io import open

DIRNAME = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(DIRNAME, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


setup(
    name='restrictsandboxed',
    version='0.1',
    description='Sandboxed processes manager',
    long_description=long_description,

    url='https://github.com/CyberAmiAsaf/DekelYigal-RestrictSandboxed',
    author='Dekel Yigal',
    author_email='dekelyi@gmail.com',

    classifiers=[
        'Development Status :: 1 - Planning',

        'Intended Audience :: Developers',
        'Topic :: System'
        'Topic :: Security',
        'Topic :: Software Development',
        'Topic :: Software Development :: Libraries :: Python Modules'

        'Programming Language :: Unix Shell',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',

        'Environment :: Console',
        'Operating System :: POSIX',
    ],
    keywords='sandbox restricted jail',
    platforms=['posix'],

    packages=find_packages(exclude=['tests']),

    install_requires=[],
    extras_require={
        'test': ['pylint', 'pytest'],
    },
)