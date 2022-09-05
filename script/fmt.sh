#!/bin/bash
# Format the TARGET (default PACKAGE) with automated code formatters
# - isort
# - black
set -eu
PACKAGE=$(dirname $(dirname $0))
TARGET=${1:-$PACKAGE}

isort --profile black $TARGET
black $TARGET
