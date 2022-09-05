#!/bin/bash

set -eu
PACKAGE=$(dirname $(dirname $0))
TARGET=${1:-$PACKAGE}

black -q --check $TARGET
flake8 $TARGET
