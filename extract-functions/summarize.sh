#!/bin/bash

HACK_ID=damqtV7yE8O5JfMk0WQw
SUBMISSION_ID=submission-2

find "data/${HACK_ID}/submissions/${SUBMISSION_ID}" \
    -name "submission_prediction_functions.js" \
    -exec cat {} \; \
    > "data/${HACK_ID}/results/${SUBMISSION_ID}/function-summary.js"
