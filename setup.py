#!/usr/bin/env python
#  This file is part of ansi2html
#  Convert ANSI (terminal) colours and attributes to HTML
#  Copyright (C) 2012  Ralph Bean <rbean@redhat.com>
#
#  Inspired by and developed off of the work by pixelbeat and blackjack.
#
#  This program is free software: you can redistribute it and/or
#  modify it under the terms of the GNU General Public License as
#  published by the Free Software Foundation, either version 3 of
#  the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
#  General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see
#  <http://www.gnu.org/licenses/>.

try:
    from setuptools import setup, find_packages
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages

import sys
import os

f = open('README.rst')
long_description = f.read().strip()
long_description = long_description.split('split here', 1)[1]
f.close()

# Ridiculous as it may seem, we need to import multiprocessing and
# logging here in order to get tests to pass smoothly on python 2.7.
try:
    # no multiprocessing in python < 2.6
    import multiprocessing
except ImportError:
    pass

import logging

requires = [
    'six',  # For python3 support
]

if sys.version_info[0] == 2 and sys.version_info[1] < 7:
    requires.append("ordereddict")

data_files = []

# We tried installing manpages with setuptools & co but it had all kinds of
# "sandbox violation" issues that were inconsistent and wonky.  Therefore, we
# don't do this anymore and instead just ship man pages with the tarball.
if False:
    # Conditionally install man pages into the system or the virtualenv.
    if 'VIRTUAL_ENV' in os.environ:
        man_prefix = os.environ['VIRTUAL_ENV']
    else:
        man_prefix = '/usr'

    data_files.append(tuple(
        man_prefix + '/share/man/man1/',
        ['man/ansi2html.1'],
    ))

version = '1.5.0'

if '--version' in sys.argv:
    print(version)
    sys.exit(0)

setup(
    name='ansi2html',
    version=version,
    description="Convert text with ANSI color codes to HTML",
    long_description=long_description,
    author='Ralph Bean',
    author_email='rbean@redhat.com',
    url='http://github.com/ralphbean/ansi2html/',
    license='LGPLv3+',
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: GNU Lesser General Public License v3 or later (LGPLv3+)",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.1",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
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
    data_files=data_files,
    include_package_data=True,
    zip_safe=False,
    entry_points="""
    [console_scripts]
    ansi2html = ansi2html.converter:main
    """
)
