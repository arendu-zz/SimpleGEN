#!/bin/bash
set -e
base="$(dirname "$0")"
#evaluate a translation
#example translation file from our paper
for s in 101 202 303; do 
  python3 eval.py "$base/"sources/mofc.en.v0.src \
    "$base/"sources/mofc.en.expected_gender \
    "$base/"outputs/mofc.seed${s}.bs1.archtransformer_vaswani_wmt_en_de_big.ngpu8.bs1.en-es.out \
    "$base"/dictionaries/dictionary-en-es-new.csv > "$base"/outputs/mofc.seed${s}.bs1.archtransformer_vaswani_wmt_en_de_big.ngpu8.bs1.en-es.result
done

