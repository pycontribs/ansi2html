#! /usr/bin/env python
import site
import sys

import setuptools

# See https://github.com/pypa/pip/issues/7953
site.ENABLE_USER_SITE = "--user" in sys.argv[1:]


if __name__ == "__main__":
    setuptools.setup(
        use_scm_version={"local_scheme": "no-local-version"},
        setup_requires=["setuptools_scm[toml]>=3.5.0"],
    )
