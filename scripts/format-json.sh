#!/bin/bash

INPUT_FILE=$1
OUTPUT_FILE=$2

jsonlint "${INPUT_FILE}" > "${OUTPUT_FILE}"
