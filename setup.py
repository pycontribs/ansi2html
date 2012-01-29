#!/usr/bin/env python

try:
    from setuptools import setup, find_packages
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages

f = open('README.rst')
long_description = f.read().strip()
long_description = long_description.split('split here', 1)[1]
f.close()

# Ridiculous as it may seem, we need to import multiprocessing and
# logging here in order to get tests to pass smoothly on python 2.7.
import multiprocessing
import logging

setup(
    name='ansi2html',
    version='0.8.1',
    description="Convert text with ANSI color codes to HTML",
    long_description=long_description,
    author='Ralph Bean',
    author_email='ralph.bean@gmail.com',
    url='http://github.com/ralphbean/ansi2html/',
    license='GPL',
    install_requires=[],
    tests_require=['nose'],
    test_suite='nose.collector',
    packages=['ansi2html'],
    include_package_data=True,
    zip_safe=False,
    entry_points="""
    [console_scripts]
    ansi2html = ansi2html.ansi2html:main
    """
)
