#!/bin/bash

INPUT_FILE=$1
OUTPUT_FILE=$2

csv2json -d "${INPUT_FILE}" > "${OUTPUT_FILE}"
