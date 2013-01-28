#!/usr/bin/env python
# -*- coding: utf-8 -*-

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


from largeman import __version__


setup(
    name='largeman',
    version='.'.join(str(x) for x in __version__),
    description='A little library for making, and using state machines.',
    url='https://github.com/sneeu/largeman',
    author='John Sutherland',
    author_email='john@sneeu.com',
    packages=['largeman'],
    license='MIT license',
    classifiers=(
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
    ),
)
