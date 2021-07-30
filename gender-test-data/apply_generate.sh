#!/bin/bash
set -e
source activate gender-bias-study

python ./generate.py terms.txt fofc.txt > fofc.en.full

python ./generate.py terms.txt momc.txt > momc.en.full

python ./generate.py terms.txt mofc.txt >  mofc.en.full

python ./generate.py terms.txt fomc.txt  > fomc.en.full

python ./generate.py terms.txt anti-stereotype.txt  > anti-stereotype.en.full
python ./generate.py terms.txt stereotype.txt  > stereotype.en.full

for ff in fofc momc fomc mofc stereotype anti-stereotype; do 
  cut -f1 $ff.en.full > $ff.en.full.new
  cut -f2- $ff.en.full > $ff.en.full.tags
done


BPEROOT=../subword-nmt
BPE_CODE=../wmt13_en_es/code.32000
python $BPEROOT/apply_bpe.py -c $BPE_CODE < fofc.en.full.new > fofc.en-es.32000.en
python $BPEROOT/apply_bpe.py -c $BPE_CODE < momc.en.full.new > momc.en-es.32000.en

python $BPEROOT/apply_bpe.py -c $BPE_CODE < mofc.en.full.new > mofc.en-es.32000.en 
python $BPEROOT/apply_bpe.py -c $BPE_CODE < fomc.en.full.new > fomc.en-es.32000.en 

python $BPEROOT/apply_bpe.py -c $BPE_CODE < stereotype.en.full.new > stereotype.en-es.32000.en 
python $BPEROOT/apply_bpe.py -c $BPE_CODE < anti-stereotype.en.full.new > anti-stereotype.en-es.32000.en 

BPE_CODE=../wmt17_en_de/code.32000
python $BPEROOT/apply_bpe.py -c $BPE_CODE < fofc.en.full.new > fofc.en-de.32000.en
python $BPEROOT/apply_bpe.py -c $BPE_CODE < momc.en.full.new > momc.en-de.32000.en

python $BPEROOT/apply_bpe.py -c $BPE_CODE < mofc.en.full.new > mofc.en-de.32000.en 
python $BPEROOT/apply_bpe.py -c $BPE_CODE < fomc.en.full.new > fomc.en-de.32000.en 

python $BPEROOT/apply_bpe.py -c $BPE_CODE < stereotype.en.full.new > stereotype.en-de.32000.en 
python $BPEROOT/apply_bpe.py -c $BPE_CODE < anti-stereotype.en.full.new > anti-stereotype.en-de.32000.en 

