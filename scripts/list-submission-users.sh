#!/bin/bash

HACK_ID="${1?'HACK_ID is required'}"
SUBMISSION_ID="submission-1"

find ./data/${HACK_ID}/submissions/${SUBMISSION_ID} -type d -printf '%P\n' \
    | sort --reverse > ./data/${HACK_ID}/${SUBMISSION_ID}/userIds
