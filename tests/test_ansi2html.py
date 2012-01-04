
from os.path import abspath, dirname, join
from ansi2html import Ansi2HTMLConverter
import cgi
import unittest

_here = dirname (abspath (__file__))

class TestAnsi2HTML (unittest.TestCase):

    def setUp(self):
        with open (join (_here, "ansicolor.txt"), "rb") as input:
            self.input = "\n".join (input.readlines ())

        with open (join (_here, "ansicolor.html"), "rb") as output:
            self.output = output.readlines ()

    def test_conversion (self):
        html = Ansi2HTMLConverter ().convert (self.input).split ("\n")

        for idx in xrange (len (self.output)):
            expected = self.output[idx].strip ()
            actual = html[idx].strip ()
            self.assertEqual (expected, actual)

    def test_partial (self):
        rainbow = '\x1b[1m\x1b[40m\x1b[31mr\x1b[32ma\x1b[33mi\x1b[34mn\x1b[35mb\x1b[36mo\x1b[37mw\x1b[0m\n'

        conv = Ansi2HTMLConverter ()
        attrs = conv.prepare (cgi.escape (rainbow))

        expected = (u'<span class="ansi1"><span class="ansi40">' +
                    u'<span class="ansi31">r<span class="ansi32">a' +
                    u'<span class="ansi33">i<span class="ansi34">n' +
                    u'<span class="ansi35">b<span class="ansi36">o' +
                    u'<span class="ansi37">w</span>\n')
        self.assertEqual (expected, attrs["body"])
        self.assertEqual ("normal", attrs["font_size"])
        self.assertTrue (attrs["dark_bg"])


if __name__ == '__main__':
    unittest.main()
