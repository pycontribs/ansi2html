#!/usr/bin/python

#Convert ANSI (terminal) colours and attributes to HTML

# Author of original sh script:
#    http://www.pixelbeat.org/docs/terminal_colours/
# Python author:
#    http://github.com/ralphbean/ansi2html/

# Is there a good Python meme off of which to model this?

headerPart1 = """
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
<style type="text/css">
/* linux console palette */
.ef0,.f0 { color: #000000; } .eb0,.b0 { background-color: #000000; }
.ef1,.f1 { color: #AA0000; } .eb1,.b1 { background-color: #AA0000; }
.ef2,.f2 { color: #00AA00; } .eb2,.b2 { background-color: #00AA00; }
.ef3,.f3 { color: #AA5500; } .eb3,.b3 { background-color: #AA5500; }
.ef4,.f4 { color: #0000AA; } .eb4,.b4 { background-color: #0000AA; }
.ef5,.f5 { color: #AA00AA; } .eb5,.b5 { background-color: #AA00AA; }
.ef6,.f6 { color: #00AAAA; } .eb6,.b6 { background-color: #00AAAA; }
.ef7,.f7 { color: #AAAAAA; } .eb7,.b7 { background-color: #AAAAAA; }
.ef8, .f0 > .bold,.bold > .f0 { color: #555555; font-weight: normal; }
.ef9, .f1 > .bold,.bold > .f1 { color: #FF5555; font-weight: normal; }
.ef10,.f2 > .bold,.bold > .f2 { color: #55FF55; font-weight: normal; }
.ef11,.f3 > .bold,.bold > .f3 { color: #FFFF55; font-weight: normal; }
.ef12,.f4 > .bold,.bold > .f4 { color: #5555FF; font-weight: normal; }
.ef13,.f5 > .bold,.bold > .f5 { color: #FF55FF; font-weight: normal; }
.ef14,.f6 > .bold,.bold > .f6 { color: #55FFFF; font-weight: normal; }
.ef15,.f7 > .bold,.bold > .f7 { color: #FFFFFF; font-weight: normal; }
.eb8  { background-color: #555555; }
.eb9  { background-color: #FF5555; }
.eb10 { background-color: #55FF55; }
.eb11 { background-color: #FFFF55; }
.eb12 { background-color: #5555FF; }
.eb13 { background-color: #FF55FF; }
.eb14 { background-color: #55FFFF; }
.eb15 { background-color: #FFFFFF; }
"""
headerPart2Light = """
.f9 { color: #AAAAAA; }
.b9 { background-color: #000000; }
.f9 > .bold,.bold > .f9, body.f9 > pre > .bold {
  /* Bold is heavy black on white, or bright white
     depending on the default background */
  color: #FFFFFF;
  font-weight: normal;
}
"""
headerPart2Dark = """
.f9 { color: #000000; }
.b9 { background-color: #AAAAAA; }
.f9 > .bold,.bold > .f9, body.f9 > pre > .bold {
  /* Bold is heavy black on white, or bright white
     depending on the default background */
  color: #000000;
  font-weight: bold;
}
"""
headerPart3 = """
.reverse {
  /* CSS doesnt support swapping fg and bg colours unfortunately,
     so just hardcode something that will look OK on all backgrounds. */
  color: #000000; background-color: #AAAAAA;
}
.underline { text-decoration: underline; }
.line-through { text-decoration: line-through; }
.blink { text-decoration: blink; }

</style>
</head>
"""

class Converter(object):
    def produceHeader(self):
        # TODO -- redo all of this with templating for sure!!
        head = headerPart1
        for re in range(5):
            for green in range(5):
                for blue in range(5):
                    c = 16 + (red * 36) + (green * 6) + blue
                    r = [red * 40 + 55, 0][ red == 0 ]
                    g = [green * 40 + 55, 0][ green == 0 ]
                    b = [blue * 40 + 55, 0][ blue == 0 ]
                    head += ".ef%d { color: #%2.2x%2.2x%2.2x; } " % (c, r, g, b)
                    head += ".eb%d { background-color: #%2.2x%2.2x%2.2x; }\n" \
                        % (c, r, g, b)
        if self.darkbg:
            head+= headerPart2Dark
        else
            head+= headerPart2Light
        head += headerPart3
        return head
    
