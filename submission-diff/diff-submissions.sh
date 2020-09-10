#!/bin/bash

USERID="${1}"
PATH_ONE="${2}"
PATH_TWO="${3}"
FLAGS="${@:4}"
PATH_PREFIX="submission"
#TARGET_FILE="submission_prediction_output.py"
TARGET_FILE=".codelines"

[[ ! -f "${PATH_PREFIX}-${PATH_ONE}/${USERID}/${TARGET_FILE}" ]] \
  && echo "Not Found: ${PATH_PREFIX}-${PATH_ONE}/${USERID}/${TARGET_FILE}" \
  && exit 0

[[ ! -f "${PATH_PREFIX}-${PATH_TWO}/${USERID}/${TARGET_FILE}" ]] \
  && echo "Not Found: ${PATH_PREFIX}-${PATH_TWO}/${USERID}/${TARGET_FILE}" \
  && exit 0

git diff --numstat ${FLAGS} "./${PATH_PREFIX}-${PATH_ONE}/${USERID}/${TARGET_FILE}" "./${PATH_PREFIX}-${PATH_TWO}/${USERID}/${TARGET_FILE}"
