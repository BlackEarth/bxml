#!/bin/bash

set -eu
PACKAGE=$(dirname $(dirname $0))
TARGET=${1:-$PACKAGE}

isort -q --profile black $TARGET
black -q $TARGET
flake8 $TARGET
