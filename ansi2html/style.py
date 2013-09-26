#    This file is part of ansi2html.
#    Copyright (C) 2012  Kuno Woudt <kuno@frob.nl>
#    Copyright (C) 2013  Sebastian Pipping <sebastian@pipping.org>
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

import sys


class Rule(object):

    def __init__(self, klass, **kw):

        self.klass = klass
        self.kw = '; '.join([(k.replace('_', '-')+': '+kw[k])
                             for k in sorted(kw.keys())]).strip()

    def __str__(self):
        return '%s { %s; }' % (self.klass, self.kw)


def index(r, g, b):
    return str(16 + (r * 36) + (g * 6) + b)


def color(r, g, b):
    return "#%.2x%.2x%.2x" % (r * 42, g * 42, b * 42)


def level(grey):
    return "#%.2x%.2x%.2x" % (((grey * 10) + 8,) * 3)


def index2(grey):
    return str(232 + grey)


def get_styles(dark_bg=True):

    css = [
        Rule('.body_foreground', color=('#000000', '#AAAAAA')[dark_bg]),
        Rule('.body_background', background_color=('#AAAAAA', '#000000')[dark_bg]),
        Rule('.body_foreground > .bold,.bold > .body_foreground, body.body_foreground > pre > .bold',
             color=('#000000', '#FFFFFF')[dark_bg], font_weight=('bold', 'normal')[dark_bg]),
        Rule('.inv_foreground', color=('#000000', '#FFFFFF')[not dark_bg]),
        Rule('.inv_background', background_color=('#AAAAAA', '#000000')[not dark_bg]),
        Rule('.ansi1', font_weight='bold'),
        Rule('.ansi3', font_style='italic'),
        Rule('.ansi4', text_decoration='underline'),
        Rule('.ansi9', text_decoration='line-through'),
        Rule('.ansi30', color="#000316"),
        Rule('.inv30', background_color="#000316"),
        Rule('.ansi31', color="#aa0000"),
        Rule('.inv31', background_color="#aa0000"),
        Rule('.ansi32', color="#00aa00"),
        Rule('.inv32', background_color="#00aa00"),
        Rule('.ansi33', color="#aa5500"),
        Rule('.inv33', background_color="#aa5500"),
        Rule('.ansi34', color="#0000aa"),
        Rule('.inv34', background_color="#0000aa"),
        Rule('.ansi35', color="#E850A8"),
        Rule('.inv35', background_color="#E850A8"),
        Rule('.ansi36', color="#00aaaa"),
        Rule('.inv36', background_color="#00aaaa"),
        Rule('.ansi37', color="#F5F1DE"),
        Rule('.inv37', background_color="#F5F1DE"),
        Rule('.ansi40', background_color="#000316"),
        Rule('.inv40', color="#000316"),
        Rule('.ansi41', background_color="#aa0000"),
        Rule('.inv41', color="#aa0000"),
        Rule('.ansi42', background_color="#00aa00"),
        Rule('.inv42', color="#00aa00"),
        Rule('.ansi43', background_color="#aa5500"),
        Rule('.inv43', color="#aa5500"),
        Rule('.ansi44', background_color="#0000aa"),
        Rule('.inv44', color="#0000aa"),
        Rule('.ansi45', background_color="#E850A8"),
        Rule('.inv45', color="#E850A8"),
        Rule('.ansi46', background_color="#00aaaa"),
        Rule('.inv46', color="#00aaaa"),
        Rule('.ansi47', background_color="#F5F1DE"),
        Rule('.inv47', color="#F5F1DE"),
        ]

    # css.append("/* Define the explicit color codes (obnoxious) */\n\n")

    for green in range(0, 6):
        for red in range(0, 6):
            for blue in range(0, 6):
                css.append(Rule(".ansi38-%s" % index(red, green, blue),
                                color=color(red, green, blue)))
                css.append(Rule(".inv38-%s" % index(red, green, blue),
                                background=color(red, green, blue)))
                css.append(Rule(".ansi48-%s" % index(red, green, blue),
                                background=color(red, green, blue)))
                css.append(Rule(".inv48-%s" % index(red, green, blue),
                                color=color(red, green, blue)))

    for grey in range(0, 24):
        css.append(Rule('.ansi38-%s' % index2(grey), color=level(grey)))
        css.append(Rule('.inv38-%s' % index2(grey), background=level(grey)))
        css.append(Rule('.ansi48-%s' % index2(grey), background=level(grey)))
        css.append(Rule('.inv48-%s' % index2(grey), color=level(grey)))

    return css
