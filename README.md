# SimpleGEN

Code for the paper Gender bias amplification during Speed-Quality optimization in Neural Machine Translation https://aclanthology.org/2021.acl-short.15/

Each source sentence has an occupation that is stereotypically female or male (according to labor statistics) and a context that indicates the person in that occupation is female or male.  For example, `People laughed at the clerk behind his back.` is a stereotypically female occupation `clerk` while `his` provides context that the person is male.

## Scoring
SimpleGEN currently supports English to Spanish and English to German translation.  

To evaluate, translate [`input.txt`](input.txt) with your translation system.  Then, presuming you wrote outputs to `output.txt`, run `./evaluate.sh de <output.txt` or `./evaluate.sh es <output.txt` depending on the target language.

## Generating from templates
We have checked in the generated source text and sidekick files.  To reproduce the generation, run `bash make_sources.sh`.  This may be useful to extend to another language.

The English sources for the test data are in `translation-inputs/*.en.src`. Each `.en.src` file has a corresponding `.en.expected_gender` meta-data file, which has wither an `m` or `f` in each line indicating whether the source context demands a masculine or feminine form of the occupation-noun in the target.

## Notes about the paper
The paper actually used the tokenization in `translation-inputs/*en.v0.src` files.  System outputs are in [`outputs/`](outputs/).
