
from os.path import abspath, dirname, join
from ansi2html import Ansi2HTMLConverter
from ansi2html.util import read_to_unicode
import cgi
import unittest
import six

_here = dirname(abspath(__file__))


class TestAnsi2HTML(unittest.TestCase):

    def test_linkify(self):
        ansi = "http://threebean.org"
        target = '<a href="http://threebean.org">http://threebean.org</a>'
        html = Ansi2HTMLConverter(linkify=True).convert(ansi)
        assert(target in html)

    def test_not_linkify(self):
        ansi = "http://threebean.org"
        target = '<a href="http://threebean.org">http://threebean.org</a>'
        html = Ansi2HTMLConverter().convert(ansi)
        assert(target not in html)

    def test_conversion(self):
        with open(join(_here, "ansicolor.txt"), "rb") as input:
            test_data = "".join(read_to_unicode(input))

        with open(join(_here, "ansicolor.html"), "rb") as output:
            expected_data = read_to_unicode(output)

        html = Ansi2HTMLConverter().convert(test_data).split("\n")

        for idx in range(len(expected_data)):
            expected = expected_data[idx].strip()
            actual = html[idx].strip()
            self.assertEqual(expected, actual)

    def test_partial(self):
        rainbow = '\x1b[1m\x1b[40m\x1b[31mr\x1b[32ma\x1b[33mi\x1b[34mn\x1b[35mb\x1b[36mo\x1b[37mw\x1b[0m\n'

        html = Ansi2HTMLConverter().convert(rainbow, full=False).strip()
        expected = (six.u('<span class="ansi1"><span class="ansi40">') +
                    six.u('<span class="ansi31">r<span class="ansi32">a') +
                    six.u('<span class="ansi33">i<span class="ansi34">n') +
                    six.u('<span class="ansi35">b<span class="ansi36">o') +
                    six.u('<span class="ansi37">w') +
                    six.u('</span>')*9)
        self.assertEqual(expected, html)

    def test_produce_headers(self):
        conv = Ansi2HTMLConverter()
        headers = conv.produce_headers().split("\n")

        inputfile = join(_here, "produce_headers.txt")
        with open(inputfile, "rb") as produce_headers:
            expected_data = read_to_unicode(produce_headers)

        for idx in range(len(expected_data)):
            expected = expected_data[idx].strip()
            actual = headers[idx].strip()
            self.assertEqual(expected, actual)

    def test_escaped_implicit(self):
        test = "<p>awesome</p>"
        expected = "&lt;p&gt;awesome&lt;/p&gt;"
        html = Ansi2HTMLConverter().convert(test, full=False)
        self.assertEqual(expected, html)

    def test_escaped_explicit(self):
        test = "<p>awesome</p>"
        expected = "&lt;p&gt;awesome&lt;/p&gt;"
        html = Ansi2HTMLConverter(escaped=True).convert(test, full=False)
        self.assertEqual(expected, html)

    def test_unescaped(self):
        test = "<p>awesome</p>"
        expected = "<p>awesome</p>"
        html = Ansi2HTMLConverter(escaped=False).convert(test, full=False)
        self.assertEqual(expected, html)

    def test_markup_lines(self):
        test = "  wat  \n "
        expected = '<span id="line-0">  wat  </span>\n<span id="line-1"> </span>'
        html = Ansi2HTMLConverter(markup_lines=True).convert(test, full=False)
        self.assertEqual(expected, html)

    def test_no_markup_lines(self):
        test = "  wat  \n "
        expected = test
        html = Ansi2HTMLConverter().convert(test, full=False)
        self.assertEqual(expected, html)

if __name__ == '__main__':
    unittest.main()
