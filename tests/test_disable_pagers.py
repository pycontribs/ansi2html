import os
from io import StringIO
from unittest.mock import patch

from tests.helpers import import_local_converter, run_with_fake_pty


@patch("sys.stdout", new_callable=StringIO)
def test_sets_git_pager_to_cat(mock_stdout: StringIO) -> None:
    conv = import_local_converter()

    # Make sure no pre-existing env overrides the default we set
    with patch.dict(os.environ, {}, clear=False):
        os.environ.pop("GIT_PAGER", None)
        # Use a simple python subprocess to echo the env var value
        script = "import os, sys; sys.stdout.write(os.environ.get('GIT_PAGER', 'NONE'))"

        # Run with PTY emulated by pipe
        run_with_fake_pty(conv, ["ansi2html", "python", "-c", script], script)

    # Our default should have been applied; content is wrapped in HTML
    assert "cat" in mock_stdout.getvalue()
