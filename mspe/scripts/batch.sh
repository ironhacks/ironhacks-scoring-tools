#!/bin/bash

SUBMISSION_ID="${1}"

echo "Running MSPE for ${SUBMISSION_ID}"

[[ -z $SUBMISSION_ID ]] && echo "No submission selected" && exit 0

[[ ! -d ../data/${SUBMISSION_ID} ]] && echo "Submission ${SUBMISSION_ID} not found" && exit 0

#TAKE THE LIST OF USERIDS AND RUN THE COMMAND FOR EACH LINE
cat ../data/${SUBMISSION_ID}/userIds | xargs -L 1 ./index.js --submission ${SUBMISSION_ID} --user

# COMBINE ALL CSVS INTO A TABLE
cd ../results/${SUBMISSION_ID}/mspe && cat *.csv | sort -u > ../mspe.csv
