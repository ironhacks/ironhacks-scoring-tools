#!/bin/bash


HACK_ID="${1}"
SUBMISSION_ID="${2}"

__convert_all_notebooks () {
    echo "No hack selected. Converting all notebooks files."
    find data/ -path "*/submissions/*" -type f -name "*.ipynb" -exec jupyter nbconvert --to script {} \;
}

__convert_hack_notebooks () {
    echo "${HACK_ID} selected. Converting submission notebooks files."
    find data/${HACK_ID} -path "*/submissions/*" -type f -name "*.ipynb" -exec jupyter nbconvert --to script {} \;
}

__convert_hack_submission_notebooks () {
    echo "${HACK_ID} selected. Converting submission notebooks files."

    [[ ! -d data/${HACK_ID}/submissions/${SUBMISSION_ID} ]] \
        && echo "Directory data/${HACK_ID}/submissions/${SUBMISSION_ID} not found" \
        && exit 0

    find data/${HACK_ID}/submissions/${SUBMISSION_ID} -type f -name "*.ipynb" -exec jupyter nbconvert --to script {} \;
}


if [ -z ${HACK_ID} ]; then
    __convert_all_notebooks
else
    if [ -z ${SUBMISSION_ID} ]; then
        __convert_hack_notebooks
    else
      __convert_hack_submission_notebooks
    fi
fi
