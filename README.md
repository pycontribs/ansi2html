[![Build Status - main branch](https://github.com/pycontribs/ansi2html/workflows/tox/badge.svg?branch=main)](https://github.com/pycontribs/ansi2html/actions?query=workflow%3Atox+branch%3Amain)

# ansi2html

Convert text with ANSI color codes to HTML or to LaTeX.

Inspired by and developed off of the work of
[pixelbeat](https://www.pixelbeat.org/docs/terminal_colours/) and
[blackjack](https://web.archive.org/web/20100911103911/http://www.koders.com/python/fid5D57DD37184B558819D0EE22FCFD67F53078B2A3.aspx).

[Read the docs](https://ansi2html.readthedocs.io/) for more
informations.

## Example - Python API

```python
from ansi2html import Ansi2HTMLConverter
conv = Ansi2HTMLConverter()
ansi = "".join(sys.stdin.readlines())
html = conv.convert(ansi)
```

## Example - Shell Usage

```shell
$ ls --color=always | ansi2html > directories.html
$ sudo tail /var/log/messages | ccze -A | ansi2html > logs.html
$ task rc._forcecolor:yes limit:0 burndown | ansi2html > burndown.html
```

See the list of full options with:

```shell
$ ansi2html --help
```

## Get this project:

```shell
$ pip3 install ansi2html
```

Source: <https://github.com/pycontribs/ansi2html/>

pypi: <https://pypi.org/project/ansi2html/>

## License

`ansi2html` is licensed LGPLv3+.

# Credits

- Author: [Ralph Bean](mailto:rbean@redhat.com)
- Contributor: [Robin Schneider](mailto:ypid23@aol.de)
