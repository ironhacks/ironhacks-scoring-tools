#!/bin/bash

# gsutil ls -lr gs://<storage_bucket>/<path>

PROJECT_ID="the-ironhacks-platform-dev"

[[ -f ".env" ]] && . "./.env"

HACK_ID=${1?'HACK_ID is required'}
SUBMISSION_ID="$2"

__list_all_submission_files () {
  gsutil ls -lr "gs://${PROJECT_ID}.appspot.com/data/hacks/${HACK_ID}"
}

__list_submission_files () {
  gsutil ls -lr "gs://${PROJECT_ID}.appspot.com/data/hacks/${HACK_ID}/${SUBMISSION_ID}"
}

if [ -z "${SUBMISSION_ID}" ]; then
  __list_all_submission_files
else
  __list_submission_files "${SUBMISSION_ID}"
fi
