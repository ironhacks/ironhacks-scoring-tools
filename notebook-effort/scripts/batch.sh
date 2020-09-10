#!/bin/bash

SUBMISSION_ID="${1}"

echo "Running Notebook Effort for ${SUBMISSION_ID}"

[[ -z $SUBMISSION_ID ]] && echo "No submission selected" && exit 0

[[ ! -d ../data/${SUBMISSION_ID} ]] && echo "Submission ${SUBMISSION_ID} not found" && exit 0

cat ../data/${SUBMISSION_ID}/userIds \
  | xargs -n 1 ./index.js --user

find ../results/${SUBMISSION_ID}/notebook-effort \
  -name "*.csv" \
  -exec cat {} \; \
    | sort --version-sort --reverse --unique \
    > "../results/${SUBMISSION_ID}/notebook-effort/${SUBMISSION_ID}-all.csv" 
