#!/bin/bash

# Remove any generated documentation
find . -name 'project*rst'
find . -name 'project*rst' -delete
# Remove LaTeX artifacts
make clean
make latex

# Build
cd build
cd latex
make LATEXMKOPTS="-lualatex"
