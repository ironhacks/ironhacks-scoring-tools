#!/bin/bash

[[ -d ./data ]] && cd ./data

[[ -d ../data ]] && cd ../data

find -type f -name "*.ipynb" -exec jupyter nbconvert --to html {} \;

find -type f -name "*.ipynb" -exec jupyter nbconvert --to script {} \;
