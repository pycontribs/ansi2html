import importlib
import os
import sys
from typing import Any, Iterable, Tuple
from unittest.mock import patch


def import_local_converter() -> Any:
    # Ensure we run the local project module, not any installed one
    mod_names = [k for k in list(sys.modules.keys()) if k.startswith("ansi2html")]
    for k in mod_names:
        sys.modules.pop(k, None)
    sys.path.insert(
        0, os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, "src"))
    )
    return importlib.import_module("ansi2html.converter")


def run_with_fake_pty(conv: Any, argv: Iterable[str], script: str) -> None:
    def _fake_openpty() -> Tuple[int, int]:
        r, w = os.pipe()
        return r, w

    with patch("sys.argv", new=list(argv)):
        with patch.object(conv.pty, "openpty", side_effect=_fake_openpty):
            conv.main()
