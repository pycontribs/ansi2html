#!/usr/bin/python

#Convert ANSI (terminal) colours and attributes to HTML

# Author of original sh script:
#    http://www.pixelbeat.org/docs/terminal_colours/
# Python author:
#    http://github.com/ralphbean/ansi2html/

import sys
import re
from genshi.template import TemplateLoader, loader
from genshi import HTML
import subprocess as sp
import chardet

class Ansi2HTMLConverter(object):
    def __init__(self, 
                 template='ansi2html.templates.default',
                 dark_bg=False,
                 font_size='large'):
        self._template = template
        self.dark_bg = dark_bg
        self.font_size = font_size
        self._attrs = None

    def prepare(self, ansi):
        """ Load the contents of 'ansi' into this object """

        # For now, make heavy use of pixelbeat's amazing script.
        p = sp.Popen(['./ansi2html.sh'],
                     stdout=sp.PIPE, stdin=sp.PIPE, shell=True)
        body = HTML(p.communicate(ansi)[0].decode('utf-8'))

        self._attrs = {
            'dark_bg' : self.dark_bg,
            'font_size' : self.font_size,
            'body' : body
        }

        return self._attrs

    def attrs(self):
        """ Prepare attributes for the template """
        if not self._attrs:
            raise Exception, "Method .prepare not yet called."
        return self._attrs

    def template(self):
        """ Load the template """
        toks = self._template.split('.')
        name, path, fname = toks[0], "/".join(toks[1:-1]), toks[-1] + '.html'
        tmpl = TemplateLoader([loader.package(name, path)]).load(fname)
        return tmpl

    def convert(self, ansi):
        return self.template().generate(**self.prepare(ansi)).render('html')

if __name__ == '__main__':
    conv = Ansi2HTMLConverter()
    ansi = " ".join(sys.stdin.readlines())
    html = conv.convert(ansi)
    print "done"
    print html

