#!/bin/bash
#Evaluate a translation
#Usage: evaluate.sh $lang <translation.txt
#$lang is either es or de
#translation.txt is the translation from en to $lang of translation-inputs/input.txt
set -eo pipefail
base="$(dirname "$0")"
lang=$1
case "$lang" in
  es)
    ;;
  de)
    ;;
  *)
    echo "Usage: $0 es <translation.txt" 1>&2
    echo "   or: $0 de <translation.txt" 1>&2
    exit 1
esac
python3 "$base"/eval.py "$base/input.txt" "$base/translation-inputs/expected_gender.txt" "$base"/dictionaries/dictionary-en-${lang}-new.csv
