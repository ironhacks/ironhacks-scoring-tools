#!/bin/bash

HACK_ID=damqtV7yE8O5JfMk0WQw
SUBMISSION_ID=submission-3

cat ./data/${HACK_ID}/results/${SUBMISSION_ID}/mspe/* \
    | sort -u -r \
    > ./data/${HACK_ID}/results/${SUBMISSION_ID}/mspe-summary.csv
