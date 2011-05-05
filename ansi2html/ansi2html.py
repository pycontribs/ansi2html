##Convert ANSI (terminal) colours and attributes to HTML
##
## Ralph Bean <ralph.bean@gmail.com>
##
## Inspired by and developed off of the work by pixelbeat and blackjack.
##
## This software may be freely redistributed under the terms of the GNU
## general public license.
##
## You should have received a copy of the GNU General Public License
## along with this program; if not, write to the Free Software
## Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.

from genshi.template import TemplateLoader, loader
from genshi import HTML
import re

class Ansi2HTMLConverter(object):
    """ Convert Ansi color codes to CSS+HTML

    Example:
    >>> conv = Ansi2HTMLConverter()
    >>> ansi = " ".join(sys.stdin.readlines())
    >>> html = conv.convert(ansi)
    """

    def __init__(self,
                 template='ansi2html.templates.default',
                 dark_bg=True,
                 font_size='normal'):
        self._template = template
        self.dark_bg = dark_bg
        self.font_size = font_size
        self._attrs = None

        self.ansi_codes_prog = re.compile( '\033\\[' '([\\d;]*)' '([a-zA-z])')

    def apply_regex(self, ansi):
        parts = self._apply_regex(ansi)
        parts = [part for part in parts]
        return "".join(parts)

    def _apply_regex(self, ansi):
        specials = {
            '&' : '&amp;',
            '<' : '&lt;',
            '>' : '&gt;',
        }
        patterns = ['&', '<', '>']
        for pattern in patterns:
            ansi = ansi.replace(pattern, specials[pattern])

        last_end = 0
        for match in self.ansi_codes_prog.finditer(ansi):
            yield ansi[last_end:match.start()]
            last_end = match.end()

            params, command = match.groups()

            if command not in 'mM':
                continue

            try:
                params = map(int, params.split(';'))
            except ValueError:
                params = [0]

            if params == [0]:
                yield '</span>'
                continue

            css_classes = " ".join(["ansi%i" % p for p in params])
            yield '<span class="%s">' % css_classes

        yield ansi[last_end:]


    def prepare(self, ansi):
        """ Load the contents of 'ansi' into this object """

        body = HTML(self.apply_regex(ansi), encoding='us-ascii')

        self._attrs = {
            'dark_bg' : self.dark_bg,
            'font_size' : self.font_size,
            'body' : body
        }

        return self._attrs

    def attrs(self):
        """ Prepare attributes for the template """
        if not self._attrs:
            raise Exception, "Method .prepare not yet called."
        return self._attrs

    def template(self):
        """ Load the template """
        toks = self._template.split('.')
        name, path, fname = toks[0], "/".join(toks[1:-1]), toks[-1] + '.html'
        tmpl = TemplateLoader([loader.package(name, path)]).load(fname)
        return tmpl

    def convert(self, ansi):
        return self.template().generate(**self.prepare(ansi)).render('html')
