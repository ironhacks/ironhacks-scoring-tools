#!/bin/bash

# REMOVES EMPTY LINES, END-OF-LINE SPACES
# AND STRIPS COMMENTS FROM SCRIPTS

INPUT_FILENAME="${1}"
OUTPUT_FILENAME=".codelines"

__strip_comments () {
  grep "^\s*#" --invert-match
}

__strip_emptylines () {
  grep -E "^[[:space:]]*$" --invert-match
}

__strip_eolspaces () {
  sed -E 's/\s*$//g'
}

cat ${INPUT_FILENAME} \
  | __strip_comments \
  | __strip_emptylines \
  | __strip_eolspaces \
  > "./${OUTPUT_FILENAME}"
