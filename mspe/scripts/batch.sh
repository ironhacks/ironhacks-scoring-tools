#!/bin/bash

HACK_ID="${1?'HACK_ID is required'}"
SUBMISSION_ID="${2?'SUBMISSION_ID is required'}"

echo "Running MSPE for ${SUBMISSION_ID}"

[[ -z $SUBMISSION_ID ]] && echo "No submission selected" && exit 0

[[ ! -d ./data/${HACK_ID}/submissions/${SUBMISSION_ID} ]] && echo "Submission ${SUBMISSION_ID} not found" && exit 0

# COMPUTE PREDICTION ACCURACY SCORES FOR EACH USER IN THE SUBMISSION
find "./data/${HACK_ID}/submissions/${SUBMISSION_ID}/" \
    -mindepth 1 \
    -type d \
    -printf '%P\n' \
    | while read USER_ID; do
        echo "reading ${HACK_ID} ${SUBMISSION_ID} ${USER_ID}"
        ./mspe/index.js --hack ${HACK_ID} --submission ${SUBMISSION_ID} --user ${USER_ID}
    done

[[ ! -d ./data/${HACK_ID}/results/${SUBMISSION_ID} ]] && echo "Submission ${SUBMISSION_ID} results path not found" && exit 0

# COMBINE ALL CSVS INTO A TABLE
cat ./data/${HACK_ID}/results/${SUBMISSION_ID}/mspe/* \
    | sort -u -r \
    > ./data/${HACK_ID}/results/${SUBMISSION_ID}/mspe-summary.csv
