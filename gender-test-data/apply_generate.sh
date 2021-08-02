#!/bin/bash
set -e
python3 ./generate.py terms.txt fofc.txt > fofc.en.full

python3 ./generate.py terms.txt momc.txt > momc.en.full

python3 ./generate.py terms.txt mofc.txt >  mofc.en.full

python3 ./generate.py terms.txt fomc.txt  > fomc.en.full

python3 ./generate.py terms.txt anti-stereotype.txt  > anti-stereotype.en.full
python3 ./generate.py terms.txt stereotype.txt  > stereotype.en.full

for ff in fofc momc fomc mofc stereotype anti-stereotype; do 
  cut -f1 $ff.en.full |sed 's/ \.$/./;s/ !$/!/;s/ , /, /g; s/ &apos;s/'\''s/g' > $ff.en.full.new
  cut -f2- $ff.en.full > $ff.en.full.tags
done
