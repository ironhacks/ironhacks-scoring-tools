#!/bin/bash


for file in {.*,*}; do cat "$file" |  grep -Eo "(http|https)://[a-zA-Z0-9./?=_-]*" | sort -u; done
