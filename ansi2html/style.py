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


class Rule(object):

    def __init__(self, klass, **kw):

        self.klass = klass
        self.kw = '; '.join([(k.replace('_', '-')+': '+kw[k])
                             for k in sorted(kw.keys())]).strip()
        self.kwl = [(k.replace('_', '-'), kw[k][1:])
                             for k in sorted(kw.keys())]

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

# Solarized color names
SOL = {
    "base03":  "#002b36",
    "base02":  "#073642",
    "base01":  "#586e75",
    "base00":  "#657b83",
    "base0":   "#839496",
    "base1":   "#93a1a1",
    "base2":   "#eee8d5",
    "base3":   "#fdf6e3",
    "yellow":  "#b58900",
    "orange":  "#cb4b16",
    "red":     "#dc322f",
    "magenta": "#d33682",
    "violet":  "#6c71c4",
    "blue":    "#268bd2",
    "cyan":    "#2aa198",
    "green":   "#859900",
}

# http://en.wikipedia.org/wiki/ANSI_escape_code#Colors
SCHEME = {
    # black red green brown/yellow blue magenta cyan grey/white
    'ansi2html': (
        "#000316", "#aa0000", "#00aa00", "#aa5500",
        "#0000aa", "#E850A8", "#00aaaa", "#F5F1DE",
        "#7f7f7f", "#ff0000", "#00ff00", "#ffff00",
        "#5c5cff", "#ff00ff", "#00ffff", "#ffffff"),

    'xterm': (
        "#000000", "#cd0000", "#00cd00", "#cdcd00",
        "#0000ee", "#cd00cd", "#00cdcd", "#e5e5e5",
        "#7f7f7f", "#ff0000", "#00ff00", "#ffff00",
        "#5c5cff", "#ff00ff", "#00ffff", "#ffffff"),

    'osx': (
        "#000000", "#c23621", "#25bc24", "#adad27",
        "#492ee1", "#d338d3", "#33bbc8", "#cbcccd") * 2,

    # http://ethanschoonover.com/solarized
    'solarized': (
        SOL["base02"], SOL["red"],     SOL["green"], SOL["yellow"],
        SOL["blue"],   SOL["magenta"], SOL["cyan"],  SOL["base2"],
        SOL["base02"], SOL["red"],     SOL["green"], SOL["yellow"],
        SOL["blue"],   SOL["magenta"], SOL["cyan"],  SOL["base2"]),

    'mint-terminal': (
        "#2E3436", "#CC0000", "#4E9A06", "#C4A000",
        "#3465A4", "#75507B", "#06989A", "#D3D7CF",
        "#555753", "#EF2929", "#8AE234", "#FCE94F",
        "#729FCF", "#AD7FA8", "#34E2E2", "#EEEEEC"),
    }

SCHEME_FG_BG = {
    'solarized-dark': (SOL["base03"], SOL["base0"]),
    'solarized-light': (SOL["base3"], SOL["base00"]),
    }

def intensify(color, dark_bg, amount=64):
    if not dark_bg:
        amount = -amount
    rgb = tuple(max(0, min(255, amount + int(color[i:i+2], 16))) for i in (1, 3, 5))
    return "#%.2x%.2x%.2x" % rgb

def get_styles(dark_bg=True, line_wrap=True, scheme='ansi2html'):
    full_scheme_name = scheme + ("-light", "-dark")[dark_bg]

    try:
        bg, fg = SCHEME_FG_BG[full_scheme_name]
        fg_bold = fg
    except KeyError:
        colors = ('#000000', '#AAAAAA')
        bg, fg = colors[not dark_bg], colors[dark_bg]
        fg_bold = ('#000000', '#FFFFFF')[dark_bg]

    css = [
        Rule('.ansi2html-content', white_space=('pre', 'pre-wrap')[line_wrap], word_wrap='break-word', display='inline'),
        Rule('.body_foreground', color=fg),
        Rule('.body_background', background_color=bg),
        Rule('.body_foreground > .bold,.bold > .body_foreground, body.body_foreground > pre > .bold',
             color=fg_bold, font_weight=('bold', 'normal')[dark_bg]),
        Rule('.inv_foreground', color=bg),
        Rule('.inv_background', background_color=fg),
        Rule('.ansi1', font_weight='bold'),
        Rule('.ansi2', font_weight='lighter'),
        Rule('.ansi3', font_style='italic'),
        Rule('.ansi4', text_decoration='underline'),
        Rule('.ansi5', text_decoration='blink'),
        Rule('.ansi6', text_decoration='blink'),
        Rule('.ansi8', visibility='hidden'),
        Rule('.ansi9', text_decoration='line-through'),
        ]

    # set palette
    pal = SCHEME[scheme]
    for _index in range(8):
        css.append(Rule('.ansi3%s' % _index, color=pal[_index]))
        css.append(Rule('.inv3%s' % _index, background_color=pal[_index]))
    for _index in range(8):
        css.append(Rule('.ansi4%s' % _index, background_color=pal[_index]))
        css.append(Rule('.inv4%s' % _index, color=pal[_index]))
    for _index in range(8):
        css.append(Rule('.ansi9%s' % _index, color=intensify(pal[_index], dark_bg)))
        css.append(Rule('.inv9%s' % _index, background_color=intensify(pal[_index], dark_bg)))
    for _index in range(8):
        css.append(Rule('.ansi10%s' % _index, background_color=intensify(pal[_index], dark_bg)))
        css.append(Rule('.inv10%s' % _index, color=intensify(pal[_index], dark_bg)))

    # set palette colors in 256 color encoding
    pal = SCHEME[scheme]
    for _index in range(len(pal)):
        css.append(Rule('.ansi38-%s' % _index, color=pal[_index]))
        css.append(Rule('.inv38-%s' % _index, background_color=pal[_index]))
    for _index in range(len(pal)):
        css.append(Rule('.ansi48-%s' % _index, background_color=pal[_index]))
        css.append(Rule('.inv48-%s' % _index, color=pal[_index]))

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
