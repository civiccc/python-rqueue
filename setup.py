#!/usr/bin/env python
import nrqueue

sdict = {
    'name' : 'nrqueue',
    'version' : nrqueue.__version__,
    'description' : 'Python client for votizen/node-redis-queue',
    'long_description' : 'Python client for votizen/node-redis-queue',
    'url': 'http://github.com/votizen/python-redis-queue',
    'author' : 'Micheil Smith',
    'author_email' : 'micheil@votizen.com',
    'maintainer' : 'Micheil Smith',
    'maintainer_email' : 'micheil@votizen.com',
    'keywords' : ['Redis', 'Queue'],
    'license' : 'MIT',
    'classifiers' : [
        'Programming Language :: Python'
    ],
    'install_requires': ['redis'],
}

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup
    
setup(**sdict)