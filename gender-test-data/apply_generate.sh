#!/bin/bash
set -e
source activate gender-bias-study

python ./generate.py terms.txt f-non-contra-templates.txt > f-non-contra-generated.en.full

python ./generate.py terms.txt m-non-contra-templates.txt > m-non-contra-generated.en.full

python ./generate.py terms.txt f-contra-templates.txt > f-contra-generated.en.full

python ./generate.py terms.txt m-contra-templates.txt > m-contra-generated.en.full


for ff in f-non-contra-generated.en.full m-non-contra-generated.en.full; do 
  cut -f1 $ff > $ff.new
  cut -f2- $ff > $ff.tags
done

for ff in f-contra-generated.en.full m-contra-generated.en.full; do 
  cut -f1 $ff > $ff.new
  cut -f2- $ff > $ff.tags
done

BPEROOT=../subword_nmt
BPE_CODE=../wmt13_en_es/code.32000
python $BPEROOT/apply_bpe.py -c $BPE_CODE < f-non-contra-generated.en.full.new > f-non-contra-en-es-generated.32000.en
python $BPEROOT/apply_bpe.py -c $BPE_CODE < m-non-contra-generated.en.full.new > m-non-contra-en-es-generated.32000.en

python $BPEROOT/apply_bpe.py -c $BPE_CODE < f-contra-generated.en.full.new > f-contra-en-es-generated.32000.en
python $BPEROOT/apply_bpe.py -c $BPE_CODE < m-contra-generated.en.full.new > m-contra-en-es-generated.32000.en

BPE_CODE=../wmt17_en_de/code.32000
python $BPEROOT/apply_bpe.py -c $BPE_CODE < f-non-contra-generated.en.full.new > f-non-contra-en-de-generated.32000.en
python $BPEROOT/apply_bpe.py -c $BPE_CODE < m-non-contra-generated.en.full.new > m-non-contra-en-de-generated.32000.en

python $BPEROOT/apply_bpe.py -c $BPE_CODE < f-contra-generated.en.full.new > f-contra-en-de-generated.32000.en
python $BPEROOT/apply_bpe.py -c $BPE_CODE < m-contra-generated.en.full.new > m-contra-en-de-generated.32000.en

