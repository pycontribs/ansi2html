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

setup(
    name='ansi2html',
    version='0.6.9',
    description="Convert text with ANSI color codes to HTML",
    long_description=long_description,
    author='Ralph Bean',
    author_email='ralph.bean@gmail.com',
    url='http://github.com/ralphbean/ansi2html/',
    license='GPL',
    install_requires=[
        "mako",
        "tw2.core", # for dottedtemplatelookup... for realsies.
    ],
    packages=['ansi2html'],
    include_package_data=True,
    zip_safe=False,
    entry_points="""
    [console_scripts]
    ansi2html = ansi2html.ansi2html:main
    """
)
