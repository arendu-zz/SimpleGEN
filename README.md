# SimpleGEN

Code for the paper Gender bias amplification during Speed-Quality optimization in Neural Machine Translation https://aclanthology.org/2021.acl-short.15/

Each source sentence has an occupation that is stereotypically female or male (according to labor statistics) and a context that indicates the person in that occupation is female or male.  For example, `People laughed at the clerk behind his back.` is a stereotypically female occupation `clerk` while `his` provides context that the person is male.

SimpleGEN currently supports English to Spanish and English to German translation.  

The English sources for the test data are in `translation-inputs/*.en.src`. Each `.en.src` file has a corresponding `.en.expected_gender` meta-data file, which has wither an `m` or `f` in each line indicating whether the source context demands a masculine or feminine form of the occupation-noun in the target.
Note that we also provide `translation-inputs/*en.v0.src` files. These contain the exact tokenization used in our paper. 

To generate the English source texts from the templates, run `bash make_sources.sh`. 

Once source files have been generated, you can evaluate the output of a translation system using the `evaluation.sh` script. As an example, we evaluate three output files generated from three models (three random seeds) used in the paper (with an extension `*.en-es.out`). The results are placed in the `outputs` folder with extension `*en-es.result`.
