#!/usr/bin/python

#Convert ANSI (terminal) colours and attributes to HTML

# Author of original sh script:
#    http://www.pixelbeat.org/docs/terminal_colours/
# Python author:
#    http://github.com/ralphbean/ansi2html/

from genshi.template import MarkupTemplate

class AnsiToHTMLConverter(object):
    def __init__(self, template='ansi2html.templates.default'):
        self.template = template
        self.attrs = {}
    
    def convert(self, ansi):
        self.prepare
        tmpl = MarkupTemplate(self.template)
        html = tmpl.generate(**self.attrs).render('html')
        return html

