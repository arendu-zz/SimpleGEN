#!/bin/bash
set -e
# create the English source files along with meta-data for evaluation
python ./generate.py terms.txt anti-stereotype.txt  > anti-stereotype.en
python ./generate.py terms.txt stereotype.txt  > stereotype.en

python ./generate.py terms.txt fofc.txt > fofc.en

python ./generate.py terms.txt momc.txt > momc.en

python ./generate.py terms.txt mofc.txt >  mofc.en

python ./generate.py terms.txt fomc.txt  > fomc.en


for ff in fofc momc fomc mofc stereotype anti-stereotype; do 
  cut -f1 $ff.en > $ff.en.src # contain the source text
  cut -f2 $ff.en > $ff.en.expected_gender # defines the expected gender for each src text
  cut -f3- $ff.en > $ff.en.tags # additional tags
done

#Run evaluation for an example output file
python ./eval.py mofc.en.src mofc.en.expected_gender ./outputs/mofc.seed101.bs1.archtransformer_vaswani_wmt_en_de_big.ngpu8.bs1.en-es.out dictionary-en-es-new.csv
