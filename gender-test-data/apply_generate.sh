#!/bin/bash
set -eo pipefail
base="$(dirname "$0")"
python3 "$base"/generate.py "$base"/terms.txt "$base"/fofc.txt > "$base"/fofc.en.full

python3 "$base"/generate.py "$base"/terms.txt "$base"/momc.txt > "$base"/momc.en.full

python3 "$base"/generate.py "$base"/terms.txt "$base"/mofc.txt > "$base"/mofc.en.full

python3 "$base"/generate.py "$base"/terms.txt "$base"/fomc.txt > "$base"/fomc.en.full

python3 "$base"/generate.py "$base"/terms.txt "$base"/anti-stereotype.txt  > "$base"/anti-stereotype.en.full
python3 "$base"/generate.py "$base"/terms.txt "$base"/stereotype.txt  > "$base"/stereotype.en.full

for ff in fofc momc fomc mofc stereotype anti-stereotype; do 
  cut -f1 "$base"/$ff.en.full |sed 's/ \.$/./;s/ !$/!/;s/ , /, /g; s/ &apos;s/'\''s/g' > "$base/"$ff.en.src
  cut -f2- "$base"/$ff.en.full > "$base/"$ff.en.tags
done
