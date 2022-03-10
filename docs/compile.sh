#!/bin/bash

find . -name 'project*rst' -delete
make clean
make latex
find . -name 'project*rst'
find . -name 'project*rst' -delete