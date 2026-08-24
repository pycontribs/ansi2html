from __future__ import annotations

from ansi2html.converter import Ansi2HTMLConverter

try:
    # pyright: reportMissingImport=false
    from ansi2html._version import __version__  # mypy: disable
except ImportError:  # pragma: no branch
    try:
        import sys

        if sys.version_info >= (3, 8):
            from importlib.metadata import version
        else:
            from importlib_metadata import version

        __version__ = version("ansi2html")
    except Exception:  # pylint: disable=broad-except
        # this is the fallback SemVer version picked by setuptools_scm when tag
        # information is not available.
        __version__ = "0.1.dev1"

__all__ = ("Ansi2HTMLConverter", "__version__")
