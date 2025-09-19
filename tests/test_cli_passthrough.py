from io import StringIO
from unittest.mock import patch

from tests.helpers import import_local_converter, run_with_fake_pty


@patch("sys.stdout", new_callable=StringIO)
def test_command_passthrough_pty_default(mock_stdout: StringIO) -> None:
    script = "import sys; sys.stdout.write('\\x1b[31mRED\\x1b[0m\\n')"
    conv = import_local_converter()
    run_with_fake_pty(conv, ["ansi2html", "python", "-c", script], script)
    out = mock_stdout.getvalue()
    assert "ansi31" in out
    assert "RED" in out


@patch("sys.stdout", new_callable=StringIO)
def test_command_passthrough_with_separator_and_inline(mock_stdout: StringIO) -> None:
    script = "import sys; sys.stdout.write('\\x1b[31mRED\\x1b[0m')"
    conv = import_local_converter()
    run_with_fake_pty(
        conv,
        ["ansi2html", "--inline", "--", "python", "-c", script],
        script,
    )
    out = mock_stdout.getvalue()
    # Inline mode should not include the full HTML template, but include styles
    assert "<html>" not in out
    assert "style=" in out or "#aa0000" in out or "ansi31" in out


@patch("sys.stdout", new_callable=StringIO)
def test_command_passthrough_with_standalone(mock_stdout: StringIO) -> None:
    script = "import sys; sys.stdout.write('\\x1b[31mRED\\x1b[0m')"
    conv = import_local_converter()
    run_with_fake_pty(
        conv,
        ["ansi2html", "--standalone", "--", "python", "-c", script],
        script,
    )
    out = mock_stdout.getvalue()
    # Standalone should not include the full HTML template, but include a <code> wrapper
    assert "<html>" not in out
    assert "<code" in out
    assert "white-space: pre;" in out
    assert "style=" in out or "#aa0000" in out or "ansi31" in out


@patch("sys.stdout", new_callable=StringIO)
def test_command_passthrough_with_standalone_shortflag(mock_stdout: StringIO) -> None:
    script = "import sys; sys.stdout.write('\\x1b[31mRED\\x1b[0m')"
    conv = import_local_converter()
    run_with_fake_pty(conv, ["ansi2html", "-S", "--", "python", "-c", script], script)
    out = mock_stdout.getvalue()
    # Short form should behave same as --standalone
    assert "<html>" not in out
    assert "<code" in out
    assert "white-space: pre;" in out
    assert "style=" in out or "#aa0000" in out or "ansi31" in out
