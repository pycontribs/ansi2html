
from os.path import abspath, dirname, join
from ansi2html import Ansi2HTMLConverter
from ansi2html.converter import main
from ansi2html.util import read_to_unicode

from mock import patch
from nose.tools import eq_

import cgi
import unittest
import six
import textwrap

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

        eq_(len(html), len(expected_data))

        for idx in range(len(expected_data)):
            expected = expected_data[idx].strip()
            actual = html[idx].strip()
            self.assertEqual(expected, actual)

    @patch("sys.argv", new_callable=lambda: ["ansi2html"])
    @patch("sys.stdout", new_callable=six.StringIO)
    def test_conversion_as_command(self, mock_stdout, mock_argv):
        with open(join(_here, "ansicolor.txt"), "rb") as input:
            test_data = "".join(read_to_unicode(input))

        with open(join(_here, "ansicolor.html"), "rb") as output:
            expected_data = "".join(read_to_unicode(output))

        if six.PY3:
            f = lambda: six.StringIO(test_data)
        else:
            f = lambda: six.StringIO(test_data.encode('utf-8'))

        with patch("sys.stdin", new_callable=f):
            main()

        html = mock_stdout.getvalue()

        eq_(len(html), len(expected_data), "Strings are not the same length.")
        eq_(html, expected_data, "Strings are not the same.")

    def test_unicode(self):
        """ Ensure that the converter returns unicode(py2)/str(py3) objs. """

        with open(join(_here, "ansicolor.txt"), "rb") as input:
            test_data = "".join(read_to_unicode(input))

        html = Ansi2HTMLConverter().convert(test_data).split("\n")

        for chunk in html:
            assert isinstance(chunk, six.text_type)

    @patch("sys.argv", new_callable=lambda: ["ansi2html", "--inline"])
    @patch("sys.stdout", new_callable=six.StringIO)
    def test_inline_as_command(self, mock_stdout, mock_argv):
        test_input = textwrap.dedent(six.u("""
        this is
        a test
        """))

        with patch("sys.stdin", new_callable=lambda: six.StringIO(test_input)):
            main()

        eq_(mock_stdout.getvalue(), test_input)

    @patch("sys.argv", new_callable=lambda: ["ansi2html", "--partial"])
    @patch("sys.stdout", new_callable=six.StringIO)
    def test_partial_as_command(self, mock_stdout, mock_argv):
        rainbow = '\x1b[1m\x1b[40m\x1b[31mr\x1b[32ma\x1b[33mi\x1b[34mn\x1b[35mb\x1b[36mo\x1b[37mw\x1b[0m\n'
        with patch("sys.stdin", new_callable=lambda: six.StringIO(rainbow)):
            main()

        html = mock_stdout.getvalue().strip()

        if hasattr(html, 'decode'):
            html = html.decode('utf-8')

        expected = (six.u('<span class="ansi1"><span class="ansi40">') +
                    six.u('<span class="ansi31">r<span class="ansi32">a') +
                    six.u('<span class="ansi33">i<span class="ansi34">n') +
                    six.u('<span class="ansi35">b<span class="ansi36">o') +
                    six.u('<span class="ansi37">w') +
                    six.u('</span>')*9)
        assert isinstance(html, six.text_type)
        assert isinstance(expected, six.text_type)
        self.assertEqual(expected, html)

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

    def test_inline(self):

        rainbow = '\x1b[1m\x1b[40m\x1b[31mr\x1b[32ma\x1b[33mi\x1b[34mn\x1b[35mb\x1b[36mo\x1b[37mw\x1b[0m'

        html = Ansi2HTMLConverter(inline=True).convert(rainbow, full=False)
        expected = (six.u('<span style="font-weight: bold">') +
                    six.u('<span style="background-color: #000316">') +
                    six.u('<span style="color: #aa0000">r<span style="color: #00aa00">a') +
                    six.u('<span style="color: #aa5500">i<span style="color: #0000aa">n') +
                    six.u('<span style="color: #E850A8">b<span style="color: #00aaaa">o') +
                    six.u('<span style="color: #F5F1DE">w') +
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
