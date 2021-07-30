#!/usr/bin/env python
# coding: utf-8
__author__ = 'adirendu'

import argparse
from itertools import product
import pdb

if __name__ == '__main__':
    opt = argparse.ArgumentParser(description="generates en text based on the templates and terms.")

    # insert options here
    opt.add_argument('terms', type=str, help='terms')
    opt.add_argument('template', type=str, help='template')
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
        for prod_vals in prod_values:
            words_copy = words[:]
            for pv, pv_position in zip(prod_vals, key_positions):
                words_copy[pv_position] = pv
            words_copy[0] = words_copy[0].capitalize()
            words_copy = ' '.join(words_copy)
            out = '\t'.join([words_copy.strip(), '\t', '\t'.join(keys)])
            print(out)

