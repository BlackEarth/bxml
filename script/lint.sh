#!/bin/bash
# Lint the TARGET (default PACKAGE) with automated linters
# - black --check
# - flake8
set -eu
PACKAGE=$(dirname $(dirname $0))
TARGET=${1:-$PACKAGE}

black -q --check $TARGET
flake8 $TARGET
