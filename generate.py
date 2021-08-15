#!/usr/bin/env python
# coding: utf-8
__author__ = 'adirendu'

import argparse
from itertools import product
import pdb

def get_expected_gender(keys):
    expected = None
    for k in keys:
        if k.startswith('[f-relationship-term') or k.startswith('[f-gender-specific'):
            assert expected is None or expected == 'f', "conflict in expected gender"
            expected = 'f'
        elif k.startswith('[m-relationship-term') or k.startswith('[m-gender-specific'):
            assert expected is None or expected == 'm', "conflict in expected gender"
            expected = 'm'
        else:
            pass
    assert expected is not None, "no expected gender after going through all keys"
    return expected

def get_occupation_gender(keys):
    occupations = [k for k in keys if k.startswith("[f-occupation") or k.startswith("[m-occupation")]
    assert len(occupations) == 1, "Expected there to be exactly one gender stereotyped occpuation"
    return occupations[0][1]

if __name__ == '__main__':
    opt = argparse.ArgumentParser(description="generates en text based on the templates and terms.")

    # insert options here
    opt.add_argument('terms', type=str, help='terms')
    opt.add_argument('template', type=str, help='template')
    #opt.add_argument('dictionary_enes', type=str, help='dictionary file for en-es')
    #opt.add_argument('dictionary_ende', type=str, help='dictionary file for en-de')
    options = opt.parse_args()
    terms = {}
    for line in open(options.terms, 'r', encoding='utf-8').readlines():
        items = line.strip().split(',')
        rem_items = [i.strip() for i in items[1:] if i.strip() != '']
        terms['[' +  items[0] + ']'] = rem_items

    for line in open(options.template, 'r', encoding='utf-8').readlines():
        words = line.strip().split()
        keys = [i for i in words if i in terms]
        key_positions = [idx for idx, i in enumerate(words) if i in terms]
        values = []
        for k in keys:
            values.append(terms[k])
        prod_values = list(product(*values))
        expected = get_expected_gender(keys)
        occpuation_gender = get_occupation_gender(keys)
        for prod_vals in prod_values:
            words_copy = words[:]
            for pv, pv_position in zip(prod_vals, key_positions):
                words_copy[pv_position] = pv
            words_copy[0] = words_copy[0].capitalize()
            words_copy = ' '.join(words_copy)
            out = '\t'.join([words_copy.strip(), expected, occpuation_gender, '\t'.join(keys)])
            print(out)
