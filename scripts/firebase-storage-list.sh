#!/bin/bash

PROJECT_ID="the-ironhacks-platform-dev"
HACK_ID="DeKE13nHvqzolDUa0Fg9"
SUBMISSION_ID="submission-3-covid-19-data-science-challenge-august-2020"

gsutil ls -l gs://${PROJECT_ID}.appspot.com/data/hacks/${HACK_ID}/${SUBMISSION_ID}
