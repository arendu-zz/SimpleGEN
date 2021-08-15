#!/bin/bash
set -eo pipefail
base="$(dirname "$0")"
python3 "$base"/generate.py "$base"/terms.txt "$base"/templates/fofc.txt > "$base"/fofc.en.full

python3 "$base"/generate.py "$base"/terms.txt "$base"/templates/momc.txt > "$base"/momc.en.full

python3 "$base"/generate.py "$base"/terms.txt "$base"/templates/mofc.txt > "$base"/mofc.en.full

python3 "$base"/generate.py "$base"/terms.txt "$base"/templates/fomc.txt > "$base"/fomc.en.full

for ff in fofc momc fomc mofc; do
  cut -f1 "$base"/$ff.en.full |sed 's/ \.$/./;s/ !$/!/;s/ , /, /g; s/ &apos;s/'\''s/g' > "$base/"translation-inputs/$ff.en.src
  cut -f1 "$base"/$ff.en.full > "$base/"translation-inputs/$ff.en.v0.src
  cut -f2-3 "$base"/$ff.en.full > "$base/"translation-inputs/$ff.en.expected_gender
  cut -f4- "$base"/$ff.en.full > "$base/"translation-inputs/$ff.en.tags
  rm "$base"/$ff.en.full 
done
cat "$base"/translation-inputs/{fofc,momc,fomc,mofc}.en.src >"$base"/input.txt
cat "$base"/translation-inputs/{fofc,momc,fomc,mofc}.en.expected_gender >"$base"/translation-inputs/expected_gender.txt
