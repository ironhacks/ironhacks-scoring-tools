#!/bin/bash

# gsutil -m cp -R gs://<storage_bucket>/<path> <destination>

PROJECT_ID="the-ironhacks-platform-dev"
HACK_ID="$1"
SUBMISSION_ID="$2"

if [ ! -d ./data/${SUBMISSION_ID} ]; then
  mkdir "./data/${SUBMISSION_ID}"
fi

gsutil -m cp -R "gs://${PROJECT_ID}.appspot.com/data/hacks/${HACK_ID}/${SUBMISSION_ID}/" "./data"


