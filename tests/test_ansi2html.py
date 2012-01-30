
from os.path import abspath, dirname, join
from ansi2html import Ansi2HTMLConverter
import cgi
import unittest

_here = dirname(abspath(__file__))


class TestAnsi2HTML(unittest.TestCase):

    def test_conversion(self):
        with open(join(_here, "ansicolor.txt"), "rb") as input:
            test_data = "".join(input.readlines())

        with open(join(_here, "ansicolor.html"), "rb") as output:
            expected_data = output.readlines()

        html = Ansi2HTMLConverter().convert(test_data).split("\n")

        for idx in xrange(len(expected_data)):
            expected = expected_data[idx].strip()
            actual = html[idx].strip()
            self.assertEqual(expected, actual)

    def test_partial(self):
        rainbow = '\x1b[1m\x1b[40m\x1b[31mr\x1b[32ma\x1b[33mi\x1b[34mn\x1b[35mb\x1b[36mo\x1b[37mw\x1b[0m\n'

        html = Ansi2HTMLConverter().convert(rainbow, full=False).strip()
        expected = (u'<span class="ansi1"><span class="ansi40">' +
                    u'<span class="ansi31">r<span class="ansi32">a' +
                    u'<span class="ansi33">i<span class="ansi34">n' +
                    u'<span class="ansi35">b<span class="ansi36">o' +
                    u'<span class="ansi37">w' +
                    u'</span>'*9)
        self.assertEqual(expected, html)

    def test_produce_headers(self):
        conv = Ansi2HTMLConverter()
        headers = conv.produce_headers().split("\n")

        inputfile = join(_here, "produce_headers.txt")
        with open(inputfile, "rb") as produce_headers:
            expected_data = produce_headers.readlines()

        for idx in xrange(len(expected_data)):
            expected = expected_data[idx].strip()
            actual = headers[idx].strip()
            self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
