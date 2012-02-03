#    This file is part of ansi2html.
#    Copyright (C) 2012  Kuno Woudt <kuno@frob.nl>
#
#    This program is free software: you can redistribute it and/or
#    modify it under the terms of the GNU General Public License as
#    published by the Free Software Foundation, either version 3 of
#    the License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
#    General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see
#    <http://www.gnu.org/licenses/>.

from __future__ import unicode_literals
from __future__ import absolute_import


def template(dark_bg=True):
    css = ["""

.body_foreground {
    color : """ + ("#AAAAAA" if dark_bg else "#000000") + """;
}

.body_background {
    background-color : """ + ("#000000" if dark_bg else "#AAAAAA") + """;
}

.body_foreground > .bold,.bold > .body_foreground, body.body_foreground > pre > .bold {
    color : """ + ("#FFFFFF" if dark_bg else "#000000") + """;
    font-weight : """ + ("normal" if dark_bg else "bold") + """;
}

.ansi1 { font-weight : bold; }
.ansi3 { font-weight : italic; }
.ansi4 { text-decoration: underline; }
.ansi9 { text-decoration: line-through; }

.ansi30 { color: #000316; }
.ansi31 { color: #aa0000; }
.ansi32 { color: #00aa00; }
.ansi33 { color: #aa5500; }
.ansi34 { color: #0000aa; }
.ansi35 { color: #E850A8; }
.ansi36 { color: #00aaaa; }
.ansi37 { color: #F5F1DE; }

.ansi40 { background-color: #000316; }
.ansi41 { background-color: #aa0000; }
.ansi42 { background-color: #00aa00; }
.ansi43 { background-color: #aa5500; }
.ansi44 { background-color: #0000aa; }
.ansi45 { background-color: #E850A8; }
.ansi46 { background-color: #00aaaa; }
.ansi47 { background-color: #F5F1DE; }
"""]

    css.append("/* Define the explicit color codes (obnoxious) */\n\n")

    def index(r, g, b):
        return str(16 + (r * 36) + (g * 6) + b)

    def color(r, g, b):
        return "#%.2x%.2x%.2x" % (r * 42, g * 42, b * 42)

    for green in range(0, 6):
        for red in range(0, 6):
            for blue in range(0, 6):
                css.append(".ansi38-%s { color: %s; }" % (
                    index(red, green, blue),
                    color(red, green, blue)
                ))
                css.append(".ansi48-%s { background: %s; }" % (
                    index(red, green, blue),
                    color(red, green, blue)
                ))

    def level(grey):
        return "#%.2x%.2x%.2x" % (((grey * 10) + 8,) * 3)

    def index2(grey):
        return str(232 + grey)

    css.append("\n")

    for grey in range(0, 24):
        css.append(".ansi38-%s { color: %s; }" % (
            index2(grey), level(grey)
        ))
        css.append(".ansi48-%s { background: %s; }" % (
            index2(grey), level(grey)
        ))

    return "\n".join(css) + "\n"
