#  This file is part of ansi2html
#  Convert ANSI (terminal) colours and attributes to HTML
#  Copyright (C) 2012  Ralph Bean <rbean@redhat.com>
#  Copyright (C) 2012  Kuno Woudt <kuno@frob.nl>
#  Copyright (C) 2012  Martin Zimmermann <info@posativ.org>
#  Copyright (C) 2013  Sebastian Pipping <sebastian@pipping.org>
#
#  Inspired by and developed off of the work by pixelbeat and blackjack.
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU Lesser General Public
#  License as published by the Free Software Foundation; either
#  version 3 of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
#  Lesser General Public License for more details.
#
#  You should have received a copy of the GNU Lesser General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.

import sys
import textwrap
from io import StringIO
from os.path import abspath, dirname, join
from subprocess import PIPE, Popen, run
from typing import List
from unittest.mock import patch

from ansi2html import Ansi2HTMLConverter
from ansi2html.converter import (
    ANSI_BLINK_FAST,
    ANSI_BLINK_OFF,
    ANSI_BLINK_SLOW,
    ANSI_INTENSITY_INCREASED,
    ANSI_INTENSITY_NORMAL,
    ANSI_INTENSITY_REDUCED,
    ANSI_NEGATIVE_OFF,
    ANSI_NEGATIVE_ON,
    ANSI_VISIBILITY_OFF,
    ANSI_VISIBILITY_ON,
    main,
)
from ansi2html.util import read_to_unicode

_here = dirname(abspath(__file__))


class TestAnsi2HTML:
    maxDiff = None

    def test_linkify(self) -> None:
        ansi = "http://threebean.org#foobar"
        target = '<a href="http://threebean.org#foobar">http://threebean.org#foobar</a>'
        html = Ansi2HTMLConverter(linkify=True).convert(ansi)
        assert target in html

    def test_not_linkify(self) -> None:
        ansi = "http://threebean.org"
        target = '<a href="http://threebean.org">http://threebean.org</a>'
        html = Ansi2HTMLConverter().convert(ansi)
        assert target not in html

    def test_osc_link(self) -> None:
        ansi = "[\x1b[01;35m\x1b[K\x1b]8;;https://gcc.gnu.org/onlinedocs/gcc/Warning-Options.html#index-Wtype-limits\x07-Wtype-limits\x1b]8;;\x07\x1b[m\x1b[K]\n"
        target = '[<span class="ansi1 ansi35"><a href="https://gcc.gnu.org/onlinedocs/gcc/Warning-Options.html#index-Wtype-limits">-Wtype-limits</a></span>]'
        html = Ansi2HTMLConverter().convert(ansi)
        assert target in html

    def test_osc_link_latex(self) -> None:
        ansi = "[\x1b[01;35m\x1b[K\x1b]8;;https://gcc.gnu.org/onlinedocs/gcc/Warning-Options.html#index-Wtype-limits\x07-Wtype-limits\x1b]8;;\x07\x1b[m\x1b[K]\n"
        target = "[\\textcolor{ansi1 ansi35}{\\href{https://gcc.gnu.org/onlinedocs/gcc/Warning-Options.html#index-Wtype-limits}{-Wtype-limits}}]"
        html = Ansi2HTMLConverter(latex=True).convert(ansi)
        assert target in html

    def test_conversion(self) -> None:
        for input_filename, expected_output_filename in (
            ("ansicolor.txt", "ansicolor.html"),
            ("ansicolor_eix.txt", "ansicolor_eix.html"),
        ):
            with open(join(_here, input_filename), "rb") as input:
                test_data = "".join(read_to_unicode(input))

            with open(join(_here, expected_output_filename), "rb") as output:
                expected_data = [e.rstrip("\n") for e in read_to_unicode(output)]

            html = (
                Ansi2HTMLConverter()
                .convert(test_data, ensure_trailing_newline=True)
                .split("\n")
            )
            if html and html[-1] == "":
                html = html[:-1]

            assert "\n".join(html) == "\n".join(expected_data)

    @patch("sys.argv", new_callable=lambda: ["ansi2html"])
    @patch("sys.stdout", new_callable=StringIO)
    def test_conversion_as_command(
        self, mock_stdout: StringIO, mock_argv: List[str]
    ) -> None:
        with open(join(_here, "ansicolor.txt"), "rb") as input:
            test_data = "".join(read_to_unicode(input))

        with open(join(_here, "ansicolor.html"), "rb") as output:
            expected_data = "".join(read_to_unicode(output))

        def f() -> StringIO:
            return StringIO(test_data)

        with patch("sys.stdin", new_callable=f):
            main()

        html = mock_stdout.getvalue()

        assert html == expected_data

    def test_unicode(self) -> None:
        """Ensure that the converter returns unicode(py2)/str(py3) objs."""

        with open(join(_here, "ansicolor.txt"), "rb") as input:
            test_data = "".join(read_to_unicode(input))

        html = Ansi2HTMLConverter().convert(test_data).split("\n")

        for chunk in html:
            assert isinstance(chunk, str)

    @patch("sys.argv", new_callable=lambda: ["ansi2html", "--inline"])
    @patch("sys.stdout", new_callable=StringIO)
    def test_inline_as_command(
        self, mock_stdout: StringIO, mock_argv: List[str]
    ) -> None:
        test_input = textwrap.dedent(
            """
        this is
        a test
        """
        )

        with patch("sys.stdin", new_callable=lambda: StringIO(test_input)):
            main()

        ms_val = mock_stdout.getvalue()
        assert ms_val == test_input, "%r != %r" % (ms_val, test_input)

    @patch("sys.argv", new_callable=lambda: ["ansi2html", "--partial"])
    @patch("sys.stdout", new_callable=StringIO)
    def test_partial_as_command(
        self, mock_stdout: StringIO, mock_argv: List[str]
    ) -> None:
        rainbow = "\x1b[1m\x1b[40m\x1b[31mr\x1b[32ma\x1b[33mi\x1b[34mn\x1b[35mb\x1b[36mo\x1b[37mw\x1b[0m\n"
        with patch("sys.stdin", new_callable=lambda: StringIO(rainbow)):
            main()

        html = mock_stdout.getvalue().strip()

        expected = (
            '<span class="ansi1"></span>'
            + '<span class="ansi1 ansi40"></span>'
            + '<span class="ansi1 ansi31 ansi40">r</span>'
            + '<span class="ansi1 ansi32 ansi40">a</span>'
            + '<span class="ansi1 ansi33 ansi40">i</span>'
            + '<span class="ansi1 ansi34 ansi40">n</span>'
            + '<span class="ansi1 ansi35 ansi40">b</span>'
            + '<span class="ansi1 ansi36 ansi40">o</span>'
            + '<span class="ansi1 ansi37 ansi40">w</span>'
        )
        assert isinstance(html, str)
        assert isinstance(expected, str)
        assert expected == html

    @patch("sys.argv", new_callable=lambda: ["ansi2html", "--headers"])
    @patch("sys.stdout", new_callable=StringIO)
    def test_headers_as_command(
        self, mock_stdout: StringIO, mock_argv: List[str]
    ) -> None:
        main()

        with open(join(_here, "produce_headers.txt"), "rb") as produce_headers:
            expected = read_to_unicode(produce_headers)

        html = mock_stdout.getvalue()

        assert isinstance(html, str)
        assert html == "".join(expected)

    def test_partial(self) -> None:
        rainbow = "\x1b[1m\x1b[40m\x1b[31mr\x1b[32ma\x1b[33mi\x1b[34mn\x1b[35mb\x1b[36mo\x1b[37mw\x1b[0m\n"

        html = Ansi2HTMLConverter().convert(rainbow, full=False).strip()
        expected = (
            '<span class="ansi1"></span>'
            + '<span class="ansi1 ansi40"></span>'
            + '<span class="ansi1 ansi31 ansi40">r</span>'
            + '<span class="ansi1 ansi32 ansi40">a</span>'
            + '<span class="ansi1 ansi33 ansi40">i</span>'
            + '<span class="ansi1 ansi34 ansi40">n</span>'
            + '<span class="ansi1 ansi35 ansi40">b</span>'
            + '<span class="ansi1 ansi36 ansi40">o</span>'
            + '<span class="ansi1 ansi37 ansi40">w</span>'
        )
        assert expected == html

    def test_inline(self) -> None:
        rainbow = "\x1b[1m\x1b[40m\x1b[31mr\x1b[32ma\x1b[33mi\x1b[34mn\x1b[35mb\x1b[36mo\x1b[37mw\x1b[0m"

        html = Ansi2HTMLConverter(inline=True).convert(rainbow, full=False)
        expected = (
            '<span style="font-weight: bold"></span>'
            + '<span style="font-weight: bold; background-color: #000316"></span>'
            + '<span style="font-weight: bold; color: #aa0000; background-color: #000316">r</span>'
            + '<span style="font-weight: bold; color: #00aa00; background-color: #000316">a</span>'
            + '<span style="font-weight: bold; color: #aa5500; background-color: #000316">i</span>'
            + '<span style="font-weight: bold; color: #0000aa; background-color: #000316">n</span>'
            + '<span style="font-weight: bold; color: #E850A8; background-color: #000316">b</span>'
            + '<span style="font-weight: bold; color: #00aaaa; background-color: #000316">o</span>'
            + '<span style="font-weight: bold; color: #F5F1DE; background-color: #000316">w</span>'
        )

        assert expected == html

    def test_produce_headers(self) -> None:
        conv = Ansi2HTMLConverter()
        headers = conv.produce_headers()

        inputfile = join(_here, "produce_headers.txt")
        with open(inputfile, "rb") as produce_headers:
            expected_data = read_to_unicode(produce_headers)

        assert headers == "".join(expected_data)

    def test_escaped_implicit(self) -> None:
        test = "<p>awesome</p>"
        expected = "&lt;p&gt;awesome&lt;/p&gt;"
        html = Ansi2HTMLConverter().convert(test, full=False)
        assert expected == html

    def test_escaped_explicit(self) -> None:
        test = "<p>awesome</p>"
        expected = "&lt;p&gt;awesome&lt;/p&gt;"
        html = Ansi2HTMLConverter(escaped=True).convert(test, full=False)
        assert expected == html

    def test_unescaped(self) -> None:
        test = "<p>awesome</p>"
        expected = "<p>awesome</p>"
        html = Ansi2HTMLConverter(escaped=False).convert(test, full=False)
        assert expected == html

    def test_markup_lines(self) -> None:
        test = "  wat  \n "
        expected = '<span id="line-0">  wat  </span>\n<span id="line-1"> </span>'
        html = Ansi2HTMLConverter(markup_lines=True).convert(test, full=False)
        assert expected == html

    def test_no_markup_lines(self) -> None:
        test = "  wat  \n "
        expected = test
        html = Ansi2HTMLConverter().convert(test, full=False)
        assert expected == html

    def test_issue_25(self) -> None:
        sample = "\x1b[0;38;5;238;48;5;231mTEXT\x1b[0m"

        html = Ansi2HTMLConverter(inline=False).convert(sample, full=False)
        expected = '<span class="ansi38-238 ansi48-231">TEXT</span>'

        assert expected == html

    def test_italic(self) -> None:
        sample = "\x1b[3mITALIC\x1b[0m"

        html = Ansi2HTMLConverter(inline=True).convert(sample, full=False)
        expected = '<span style="font-style: italic">ITALIC</span>'

        assert expected == html

    def test_hidden_text(self) -> None:
        sample = "\x1b[%dmHIDDEN\x1b[%dmVISIBLE\x1b[0m" % (
            ANSI_VISIBILITY_OFF,
            ANSI_VISIBILITY_ON,
        )

        html = Ansi2HTMLConverter(inline=True).convert(sample, full=False)
        expected = '<span style="visibility: hidden">HIDDEN</span>VISIBLE'

        assert expected == html

    def test_lighter_text(self) -> None:
        sample = "NORMAL\x1b[%dmLIGHTER\x1b[%dmBOLD\x1b[%dmNORMAL" % (
            ANSI_INTENSITY_REDUCED,
            ANSI_INTENSITY_INCREASED,
            ANSI_INTENSITY_NORMAL,
        )

        html = Ansi2HTMLConverter(inline=True).convert(sample, full=False)
        expected = 'NORMAL<span style="font-weight: lighter">LIGHTER</span><span style="font-weight: bold">BOLD</span>NORMAL'

        assert expected == html

    def test_blinking_text(self) -> None:
        sample = "\x1b[%dm555\x1b[%dm666\x1b[%dmNOBLINK\x1b[0m" % (
            ANSI_BLINK_SLOW,
            ANSI_BLINK_FAST,
            ANSI_BLINK_OFF,
        )

        html = Ansi2HTMLConverter(inline=True).convert(sample, full=False)
        expected = '<span style="text-decoration: blink">555</span><span style="text-decoration: blink">666</span>NOBLINK'
        assert expected == html

        html = Ansi2HTMLConverter(inline=False).convert(sample, full=False)
        expected = '<span class="ansi5">555</span><span class="ansi6">666</span>NOBLINK'
        assert expected == html

    def test_inverse_text(self) -> None:
        sample = "NORMAL\x1b[%dmINVERSE\x1b[%dmNORMAL\x1b[0m" % (
            ANSI_NEGATIVE_ON,
            ANSI_NEGATIVE_OFF,
        )
        html = Ansi2HTMLConverter(inline=False).convert(sample, full=False)
        expected = (
            'NORMAL<span class="inv_background inv_foreground">INVERSE</span>NORMAL'
        )
        assert expected == html

        sample = "NORMAL\x1b[%dm303030\x1b[%dm!30!30!30\x1b[%dm303030\x1b[0m" % (
            30,
            ANSI_NEGATIVE_ON,
            ANSI_NEGATIVE_OFF,
        )
        html = Ansi2HTMLConverter(inline=False).convert(sample, full=False)
        expected = 'NORMAL<span class="ansi30">303030</span><span class="inv30 inv_foreground">!30!30!30</span><span class="ansi30">303030</span>'
        assert expected == html

        sample = (
            "NORMAL\x1b[%dm313131\x1b[%dm!31!31!31\x1b[%dm!31!43\x1b[%dm31+43\x1b[0mNORMAL"
            % (31, ANSI_NEGATIVE_ON, 43, ANSI_NEGATIVE_OFF)
        )
        html = Ansi2HTMLConverter(inline=False).convert(sample, full=False)
        expected = 'NORMAL<span class="ansi31">313131</span><span class="inv31 inv_foreground">!31!31!31</span><span class="inv31 inv43">!31!43</span><span class="ansi31 ansi43">31+43</span>NORMAL'
        assert expected == html

    def test_cross_line_state(self) -> None:  # covers issue 36, too
        sample = "\x1b[31mRED\nSTILL RED"
        html = Ansi2HTMLConverter(inline=True).convert(
            sample, full=False, ensure_trailing_newline=False
        )
        expected = '<span style="color: #aa0000">RED\nSTILL RED</span>'
        assert expected == html

        sample = "\x1b[31mRED\nSTILL RED\n"
        html = Ansi2HTMLConverter(inline=True).convert(
            sample, full=False, ensure_trailing_newline=False
        )
        expected = '<span style="color: #aa0000">RED\nSTILL RED\n</span>'
        assert expected == html

        sample = "\x1b[31mRED\nSTILL RED"
        html = Ansi2HTMLConverter(inline=True).convert(
            sample, full=False, ensure_trailing_newline=True
        )
        expected = '<span style="color: #aa0000">RED\nSTILL RED</span>\n'
        assert expected == html

        sample = "\x1b[31mRED\nSTILL RED\n"
        html = Ansi2HTMLConverter(inline=True).convert(
            sample, full=False, ensure_trailing_newline=True
        )
        expected = '<span style="color: #aa0000">RED\nSTILL RED\n</span>\n'
        assert expected == html

        sample = "\x1b[31mRED\nSTILL RED\x1b[m\n"
        html = Ansi2HTMLConverter(inline=True).convert(
            sample, full=False, ensure_trailing_newline=True
        )
        expected = '<span style="color: #aa0000">RED\nSTILL RED</span>\n'
        assert expected == html

    def test_scheme(self) -> None:  # covers issue 36, too
        sample = "\x1b[33mYELLOW/BROWN"
        # ansi2html scheme is brown #aa5500
        html = Ansi2HTMLConverter(inline=True).convert(
            sample, full=False, ensure_trailing_newline=False
        )
        expected = '<span style="color: #aa5500">YELLOW/BROWN</span>'
        assert expected == html

        # xterm scheme is yellow #cdcd00
        html = Ansi2HTMLConverter(inline=True, scheme="xterm").convert(
            sample, full=False, ensure_trailing_newline=False
        )
        expected = '<span style="color: #cdcd00">YELLOW/BROWN</span>'
        assert expected == html

    def test_latex_inline(self) -> None:
        ansi = "\x1b[33mYELLOW/BROWN"
        target = "\\textcolor[HTML]{aa5500}{YELLOW/BROWN}"
        latex = Ansi2HTMLConverter(latex=True, inline=True).convert(ansi)
        assert target in latex

    def test_latex_title(self) -> None:
        ansi = ""
        title = "testing"
        target = "\\title{%s}" % title
        latex = Ansi2HTMLConverter(latex=True, inline=True, title=title).convert(ansi)
        assert target in latex

    def test_latex_linkify(self) -> None:
        ansi = "http://python.org/"
        target = "\\url{%s}" % ansi
        latex = Ansi2HTMLConverter(latex=True, inline=True, linkify=True).convert(ansi)
        assert target in latex

    def test_truecolor(self) -> None:
        ansi = (
            "\u001b[38;2;255;102;102m 1 \u001b[0m "
            + "\u001b[38;2;0;0;255m 2 \u001b[0m "
            + "\u001b[48;2;65;105;225m 3 \u001b[0m"
        )
        target = (
            '<span class="ansi38-255102102"> 1 </span> '
            + '<span class="ansi38-000000255"> 2 </span> '
            + '<span class="ansi48-065105225"> 3 </span>'
        )
        html = Ansi2HTMLConverter().convert(ansi)
        assert target in html

    def test_truecolor_inline(self) -> None:
        ansi = (
            "\u001b[38;2;255;102;102m 1 \u001b[0m "
            + "\u001b[38;2;0;0;255m 2 \u001b[0m "
            + "\u001b[48;2;65;105;225m 3 \u001b[0m"
        )
        target = (
            '<span style="color: #FF6666"> 1 </span> '
            + '<span style="color: #0000FF"> 2 </span> '
            + '<span style="background-color: #4169E1"> 3 </span>'
        )
        html = Ansi2HTMLConverter(inline=True).convert(ansi)
        assert target in html

    def test_truecolor_malformed(self) -> None:
        ansi = "\u001b[38;2;255;102m malformed \u001b[0m "
        #                         ^ e.g. ";102" missed
        target = '<span class="ansi2 ansi102"> malformed </span> '
        html = Ansi2HTMLConverter().convert(ansi)
        assert target in html

    def test_256_color_malformed(self) -> None:
        ansi = "\u001b[38;5m malformed \u001b[0m "
        #                 ^ e.g. ";255" missed
        target = '<span class="ansi5"> malformed </span> '
        html = Ansi2HTMLConverter().convert(ansi)
        assert target in html

    def test_x_bit_color_malformed(self) -> None:
        ansi = "\u001b[38m malformed \u001b[0m "
        #               ^ e.g. ";5;255m" missed
        target = '<span class="ansi38"> malformed </span> '
        html = Ansi2HTMLConverter().convert(ansi)
        assert target in html

    def test_command_script(self) -> None:
        result = run(["ansi2html", "--version"], check=True)
        assert result.returncode == 0

    def test_command_input_output_encoding(self) -> None:
        input_encoding = "utf-16"
        input_bytes = "regular \033[31mred\033[0m regular".encode(input_encoding)
        output_encoding = "utf-32"
        output_bytes_expected = (
            'regular <span style="color: #aa0000">red</span> regular\n'.encode(
                output_encoding
            )
        )

        with Popen(
            [
                "ansi2html",
                "--inline",
                f"--input-encoding={input_encoding}",
                f"--output-encoding={output_encoding}",
            ],
            stdin=PIPE,
            stdout=PIPE,
        ) as process:
            assert process.stdin  # for mypy
            assert process.stdout  # for mypy
            process.stdin.write(input_bytes)
            process.stdin.close()
            stdout_bytes_actual = process.stdout.read()

        assert stdout_bytes_actual == output_bytes_expected
        assert process.returncode == 0

    def test_command_module(self) -> None:
        result = run([sys.executable, "-m", "ansi2html", "--version"], check=True)
        assert result.returncode == 0
