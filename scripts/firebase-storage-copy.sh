#!/bin/bash

# gsutil -m cp -R gs://<storage_bucket>/<path> <destination>

PROJECT_ID="the-ironhacks-platform-dev"
HACK_ID="damqtV7yE8O5JfMk0WQw"

[[ -f ".env" ]] && . "./.env"

SUBMISSION_ID=$1

__get_all_submission_files () {
  if [ ! -d "./data/${HACK_ID}/submissions" ]; then
    mkdir "./data/${HACK_ID}/submissions"
  fi

  gsutil -m cp -R "gs://${PROJECT_ID}.appspot.com/data/hacks/${HACK_ID}" "./data/${HACK_ID}/submissions/"
}

__get_submission_files () {
  if [ ! -d "./data/${HACK_ID}" ]; then
    mkdir "./data/${HACK_ID}/submissions"
  fi

  if [ ! -d "./data/${HACK_ID}/submissions/${SUBMISSION_ID}" ]; then
    mkdir "./data/${HACK_ID}/submissions/${SUBMISSION_ID}"
  fi

  gsutil -m cp -R "gs://${PROJECT_ID}.appspot.com/data/hacks/${HACK_ID}/${SUBMISSION_ID}" "./data/${HACK_ID}/submissions/"
}

if [ ! -d "./data/${HACK_ID}" ]; then
  mkdir "./data/${HACK_ID}"
fi

if [ -z "${SUBMISSION_ID}" ]; then
  __get_all_submission_files
else
  __get_submission_files "${SUBMISSION_ID}"
fi
