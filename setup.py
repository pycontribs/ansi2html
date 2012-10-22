#!/usr/bin/env python

try:
    from setuptools import setup, find_packages
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages

import sys

f = open('README.rst')
long_description = f.read().strip()
long_description = long_description.split('split here', 1)[1]
f.close()

# Ridiculous as it may seem, we need to import multiprocessing and
# logging here in order to get tests to pass smoothly on python 2.7.

# no multiprocessing in python < 2.6
#import multiprocessing
import logging

requires = [
    'six',  # For python3 support
]

if sys.version_info[0] == 2 and sys.version_info[1] < 7:
    requires.append("ordereddict")

setup(
    name='ansi2html',
    version='0.9.3',
    description="Convert text with ANSI color codes to HTML",
    long_description=long_description,
    author='Ralph Bean',
    author_email='rbean@redhat.com',
    url='http://github.com/ralphbean/ansi2html/',
    license='GPLv3+',
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.1",
        "Programming Language :: Python :: 3.2",
        "Topic :: Text Processing",
        "Topic :: Text Processing :: Markup",
        "Topic :: Text Processing :: Markup :: HTML",
    ],
    install_requires=requires,
    tests_require=[
        'nose',
        'mock>=0.8',
    ],
    test_suite='nose.collector',
    packages=['ansi2html'],
    include_package_data=True,
    zip_safe=False,
    entry_points="""
    [console_scripts]
    ansi2html = ansi2html.converter:main
    """
)
