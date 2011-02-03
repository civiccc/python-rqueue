#!/usr/bin/env python
from queue import __version__

sdict = {
    'name' : 'votizen-redis-queue',
    'version' : __version__,
    'description' : 'Python client for votizen/node-redis-queue',
    'long_description' : 'Python client for votizen/node-redis-queue',
    'url': 'http://github.com/votizen/python-redis-queue',
    'author' : 'Micheil Smith',
    'author_email' : 'micheil@votizen.com',
    'maintainer' : 'Micheil Smith',
    'maintainer_email' : 'micheil@votizen.com',
    'keywords' : ['Redis', 'Queue'],
    'license' : 'MIT',
    'packages' : ['redis'],
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