#!/usr/bin/env bash

echo "Running autopep..."
find -type f -name '*.py' -exec autopep8 --in-place --aggressive --aggressive '{}' \;