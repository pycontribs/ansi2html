#!/usr/bin/python

#Convert ANSI (terminal) colours and attributes to HTML

# Author of original sh script:
#    http://www.pixelbeat.org/docs/terminal_colours/
# Python author:
#    http://github.com/ralphbean/ansi2html/

from genshi.template import TemplateLoader, loader

class Ansi2HTMLConverter(object):
    def __init__(self, template='ansi2html.templates.default'):
        self._template = template
        self._attrs = None

    def prepare(self, ansi):
        """ Load the contents of 'ansi' into this object """
        self._attrs = {}
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
    html = conv.convert('foo')
    print "done"
    print html

