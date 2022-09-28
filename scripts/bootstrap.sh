#!/bin/bash

# script/bootstrap: Resolve all requirements that the application requires to build.

echo "==> bootstrap begin"

echo "==> Set Console Settings"
set -euo pipefail
IFS=$'\n\t'

script_dir=`dirname $0`

echo "==> Install Requirements"
python -m pip install --upgrade pip
pip3 install --user -r $script_dir/../requirements.txt
curl -sSL https://install.python-poetry.org | python3 -

echo "==> Reset Console Settings"
set +euo pipefail

echo "==> bootstrap complete"