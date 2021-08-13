#!/bin/bash
set -eo pipefail
base="$(dirname "$0")"
python3 "$base"/generate.py "$base"/terms.txt "$base"/templates/fofc.txt > "$base"/fofc.en.full

python3 "$base"/generate.py "$base"/terms.txt "$base"/templates/momc.txt > "$base"/momc.en.full

python3 "$base"/generate.py "$base"/terms.txt "$base"/templates/mofc.txt > "$base"/mofc.en.full

python3 "$base"/generate.py "$base"/terms.txt "$base"/templates/fomc.txt > "$base"/fomc.en.full

python3 "$base"/generate.py "$base"/terms.txt "$base"/templates/anti-stereotype.txt  > "$base"/anti-stereotype.en.full
python3 "$base"/generate.py "$base"/terms.txt "$base"/templates/stereotype.txt  > "$base"/stereotype.en.full

for ff in fofc momc fomc mofc stereotype anti-stereotype; do 
  cut -f1 "$base"/$ff.en.full |sed 's/ \.$/./;s/ !$/!/;s/ , /, /g; s/ &apos;s/'\''s/g' > "$base/"sources/$ff.en.src
  cut -f1 "$base"/$ff.en.full > "$base/"sources/$ff.en.v0.src
  cut -f2- "$base"/$ff.en.full > "$base/"sources/$ff.en.expected_gender
  cut -f3- "$base"/$ff.en.full > "$base/"sources/$ff.en.tags
  \rm "$base"/$ff.en.full 
done

