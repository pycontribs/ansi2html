# Copyright (C) 2013 Sebastian Pipping <sebastian@pipping.org>
# Licensed under GPL v3 or later

DESTDIR = /
SETUP_PY = ./setup.py

all:
	$(SETUP_PY) build

check:
	$(SETUP_PY) check
	$(SETUP_PY) test

clean:
	$(SETUP_PY) clean

dist:
	$(SETUP_PY) sdist

install:
	$(SETUP_PY) install --root '$(DESTDIR)'

.PHONY: all check clean dist install
