#!/usr/bin/env python

import sys
from ansi2html import Ansi2HTMLConverter

if __name__ == '__main__':
    conv = Ansi2HTMLConverter()
    ansi = " ".join(sys.stdin.readlines())
    html = conv.convert(ansi)
    print html

