# Copyright (C) 2013 Sebastian Pipping <sebastian@pipping.org>
# Licensed under LGPL v3 or later

DESTDIR = /
SETUP_PY = ./setup.py

A2X = a2x
PYTHON = python
RM = rm

GENERATED_FILES = man/ansi2html.1

_MANUAL_PACKAGE = ansi2html
_MANUAL_TITLE = ansi2html Manual
_MANUAL_VERSION = $(shell $(PYTHON) setup.py --version)


all: $(GENERATED_FILES)
	$(SETUP_PY) build

check: $(GENERATED_FILES)
	$(SETUP_PY) check
	$(SETUP_PY) test

clean:
	$(SETUP_PY) clean
	$(RM) -f $(GENERATED_FILES)

dist: $(GENERATED_FILES)
	$(SETUP_PY) sdist

upload: $(GENERATED_FILES)
	$(SETUP_PY) sdist upload --sign

install: $(GENERATED_FILES)
	$(SETUP_PY) install --root '$(DESTDIR)'

man/ansi2html.1: man/ansi2html.1.txt man/asciidoc.conf Makefile setup.py
	$(A2X) \
		--conf-file=man/asciidoc.conf \
		--attribute="manual_package=$(_MANUAL_PACKAGE)" \
		--attribute="manual_title=$(_MANUAL_TITLE)" \
		--attribute="manual_version=$(_MANUAL_VERSION)" \
		--format=manpage -D man \
		"$<"

.PHONY: all check clean dist install upload
