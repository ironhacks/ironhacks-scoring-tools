#!/bin/bash

TARGET_FILE="submission_prediction_output.py"

find . -type f -name ${TARGET_FILE} -execdir bash ../../format-submissions.sh {} \;
