#!/usr/bin/env python
# coding: utf-8
__author__ = 'adirendu'

import argparse
import re
import pdb

if __name__ == '__main__':
    opt = argparse.ArgumentParser(description="evals gender noun translation against a dictionary")

    # insert options here
    opt.add_argument('outfile', type=str, help='translation output from fairseq interactive')
    opt.add_argument('dictionary', type=str, help='En-Es to En-De dictionary file')
    opt.add_argument('mode', type=str, help='(f/m) expects fem-gender nouns or masc-gender-nouns in the output translation')
    options = opt.parse_args()

    outfile_pairs = {}
    srcs = []
    hyps= []
    alignments = []
    for line in open(options.outfile, 'r', encoding='utf-8').readlines():
        line = line.strip()
        if line.startswith('S-'):
            srcs.append(' '.join(line.strip().split()[1:]))
        if line.startswith('H-'):
            hyps.append(' '.join(line.strip().split()[2:]))
        if line.startswith('A-'):
            alignments.append(line.strip().split()[1:])

    #print(len(srcs), len(hyps), len(alignments))


    dictionary = {}
    all_fem_opts = []
    all_masc_opts = []
    for line in open(options.dictionary, 'r', encoding='utf-8').readlines():
        eng, tgt_masc, tgt_fem = line.strip().split(',')
        tgt_masc = tgt_masc.lower()
        tgt_fem = tgt_fem.lower()
        tgt_masc_opts = [i.strip() for i in tgt_masc.split('|')]
        tgt_fem_opts = [i.strip() for i in tgt_fem.split('|')]
        all_fem_opts += tgt_fem_opts
        all_masc_opts += tgt_masc_opts
        #assert len(tgt_fem_opts) == len(tgt_masc_opts)
        dictionary[eng.lower()] = (tgt_masc_opts, tgt_fem_opts)

    incorrects = []
    corrects = []
    wrongs = []
    not_wrongs = []
    idx = 0
    for src, hyp, alignment in zip(srcs, hyps, alignments):
        #print(src)
        idx += 1
        for k, v in dictionary.items():
            k_re = re.compile(r'\b%s\b' % k, re.I)
            if k_re.search(src.lower()):
                m_exp_opts, f_exp_opts = dictionary[k]
                if options.mode == 'f':
                    exps = f_exp_opts
                    wrgs = m_exp_opts + all_masc_opts
                else:
                    exps = m_exp_opts
                    wrgs = f_exp_opts + all_fem_opts

                found_match  = False
                for exp in exps:
                    m = re.compile(r'\b%s\b' % exp, re.I)
                    if m.search(hyp):
                        found_match = True
                        corrects.append((k, exp, src, hyp))
                        print(idx, 'correct', ' || '.join([k, exp, src, hyp]))
                        break

                if not found_match:
                    found_wrong = False
                    for wrg in wrgs:
                        m = re.compile(r'\b%s\b' % wrg, re.I)
                        if m.search(hyp):
                            found_wrong = True
                            wrongs.append((k, exps, wrg, src, hyp))
                            print(idx, 'wrong', ' || '.join([k, '|'.join(exps), wrg, src, hyp]))
                            break

                if not found_match and not found_wrong:
                    incorrects.append((k, exps, src, hyp))
                    print(idx, 'incorrect', ' || '.join([k, '|'.join(exps), src, hyp]))
                break
