#!/bin/bash

# Remove any previous documentation
find . -name '~REPLACE-BY-CODENAME~*rst'
find . -name '~REPLACE-BY-CODENAME~*rst' -delete
# Clean
make clean

# Generate site
make html
find . -name '~REPLACE-BY-CODENAME~*rst'
find . -name '~REPLACE-BY-CODENAME~*rst' -delete

# Remove LaTeX artifacts
make latex
find . -name '~REPLACE-BY-CODENAME~*rst'
find . -name '~REPLACE-BY-CODENAME~*rst' -delete

# Build
cd build
cd latex
make LATEXMKOPTS="-lualatex"
