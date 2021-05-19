#!/bin/bash
# This shell script builds the apidocs for ansi2html

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"

# Stop if errors
set -euo pipefail
IFS=$'\n\t,'

# Figure the project version
project_version="$(python3 setup.py -V)"

# Figure commit ref
git_sha="$(git rev-parse HEAD)"
if ! git describe --exact-match --tags > /dev/null 2>&1 ; then
    is_tag=false
else
    git_sha="$(git describe --exact-match --tags)"
    is_tag=true
fi

# Init docs folder
docs_folder="$SCRIPT_DIR/build/apidocs"
rm -rf "${docs_folder}"
mkdir -p "${docs_folder}"

# Run pydoctor build
pydoctor \
    --project-name="ansi2html ${project_version}" \
    --project-url="https://github.com/pycontribs/ansi2html/" \
    --html-viewsource-base="https://github.com/pycontribs/ansi2html/tree/${git_sha}" \
    --make-html --quiet -W \
    --project-base-dir="$SCRIPT_DIR"\
    --docformat=restructuredtext \
    --intersphinx=https://docs.python.org/3/objects.inv \
    --html-output="${docs_folder}" \
    ./ansi2html

echo "API docs generated in ${docs_folder}"
