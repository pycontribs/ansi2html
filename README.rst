ansi2html
=========

:Author: Ralph Bean <rbean@redhat.com>

.. comment: split here

Convert text with ANSI color codes to HTML

.. _pixelbeat: http://www.pixelbeat.org/docs/terminal_colours/
.. _blackjack: http://www.koders.com/python/fid5D57DD37184B558819D0EE22FCFD67F53078B2A3.aspx

Inspired by and developed off of the work of `pixelbeat`_ and `blackjack`_.

Forked by Jens Timmerman for easy installation in python 2.4


Example - Python API
--------------------

>>> from ansi2html import Ansi2HTMLConverter
>>> conv = Ansi2HTMLConverter()
>>> ansi = " ".join(sys.stdin.readlines())
>>> html = conv.convert(ansi)

Example - Shell Usage
---------------------

::

 $ ls --color=always | ansi2html > directories.html
 $ sudo tail /var/log/messages | ccze -A | ansi2html > logs.html
 $ task burndown | ansi2html > burndown.html

See the list of full options with::

 $ ansi2html --help

Get this project:
-----------------

::

 $ sudo easy_install -v -Z https://github.com/JensTimmerman/ansi2html/tarball/develop#egg=ansi2html-0.9.2

Source: https://github.com/JensTimmerman/ansi2html

Original Source:  http://github.com/ralphbean/ansi2html/

pypi:    http://pypi.python.org/pypi/ansi2html/

License
-------

``ansi2html`` is licensed GPLv3+.
