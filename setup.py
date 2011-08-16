#!/usr/bin/env python

sdict = dict(
    name = 'rqueue',
    packages = ['rqueue'],
    version = '0.4.0',
    description = 'Python client for votizen/node-rqueue',
    long_description = 'Python client for votizen/node-rqueue',
    url = 'http://github.com/votizen/python-rqueue',
    author = 'Matt Snider',
    author_email = 'msnider@votizen.com',
    maintainer = 'Matt Snider',
    maintainer_email = 'msnider@votizen.com',
    keywords = ['Redis', 'Queue'],
    license = 'MIT',
    classifiers=[
        'Programming Language :: Python',
        'license :: MIT',
        'Operating System :: OS Independent',
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    install_requires = ['redis', 'uuid'],
)

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(**sdict)
