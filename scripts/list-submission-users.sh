#!/bin/bash

SUBMISSION_ID="submission-1"

find ../data/${SUBMISSION_ID} -type d -printf '%P\n' | sort --reverse > ../data/${SUBMISSION_ID}/userIds
