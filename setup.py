#!/usr/bin/env python

sdict = {
    'name' : 'rqueue',
    'version' : '0.0.4',
    'description' : 'Python client for votizen/node-rqueue',
    'long_description' : 'Python client for votizen/node-rqueue',
    'url': 'http://github.com/votizen/python-rqueue',
    'author' : 'Micheil Smith',
    'author_email' : 'micheil@votizen.com',
    'maintainer' : 'Micheil Smith',
    'maintainer_email' : 'micheil@votizen.com',
    'keywords' : ['Redis', 'Queue'],
    'license' : 'MIT',
    'classifiers' : [
        'Programming Language :: Python'
    ],
    'install_requires': ['redis', 'uuid'],
}

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup
    
setup(**sdict)
