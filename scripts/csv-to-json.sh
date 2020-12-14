#!/bin/bash

INPUT_FILE=${1?'Input file is required'}
OUTPUT_FILE=${2?'Output file is required'}

# REQUIRES CSV2JSON
# INSTALL: npm i -g csv2json

csv2json -d "${INPUT_FILE}" > "${OUTPUT_FILE}"
