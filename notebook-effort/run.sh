#!/bin/bash

HACK_ID=${1?'HACK_ID is required'}
SUBMISSION_ID=${2?'SUBMISSION_ID is required'}
USER_ID=${3?'USER_ID is required'}

echo "Extracting functions from ${USER_ID}"

./notebook-effort/index.js --hack ${HACK_ID} --submission ${SUBMISSION_ID} --user ${USER_ID}
