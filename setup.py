#!/usr/bin/env python


try:
    from setuptools import setup, find_packages
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages

from setuptools.command.install import install as _install
import os
import stat as s

class install(_install):
    def run(self):
        _install.run(self)
        script = "%s/ansi2html/ansi2html.sh" % self.install_libbase 
        mode = s.S_IRUSR | s.S_IWUSR | s.S_IXUSR | s.S_IROTH | s.S_IXOTH
        os.chmod(script, mode)

setup(
    cmdclass={'install': install},
    name='ansi2html',
    version='0.4',
    description="Python Wrapper for pixelbeat.org's ansi2html.sh",
    long_description=open('README.md').read(),
    author='Ralph Bean',
    author_email='ralph.bean@gmail.com',
    url='http://github.com/ralphbean/ansi2html/',
    install_requires=[
        "genshi",
    ],
    packages=['ansi2html'],
    package_data={ 'ansi2html' : [ 'ansi2html.sh', 'templates/*' ], },
)
