#!/usr/bin/env python
# coding: utf-8
__author__ = 'adirendu'

import argparse
import io
import re
import sys

class Stats:
    def __init__(self):
        self.right = 0
        self.wrong = 0
        self.inconclusive = 0
    def total(self):
        return self.right + self.wrong + self.inconclusive
    def __iadd__(self, other):
        self.right += other.right
        self.wrong += other.wrong
        self.inconclusive += other.inconclusive
    def __add__(self, other):
        ret = Stats()
        ret.right = self.right + other.right
        ret.wrong = self.wrong + other.wrong
        ret.inconclusive = self.inconclusive + other.inconclusive
        return ret
    def __str__(self):
        return "{: >4d} {:5.2f}% {: >4d} {:5.2f}% {:>4d} {:5.2f}%".format(self.right, self.right / self.total() * 100.0, self.wrong, self.wrong / self.total() * 100.0, self.inconclusive, self.inconclusive / self.total() * 100.0)

class Buckets:
    def __init__(self):
        self.map = {
            ('f', 'f') : Stats(),
            ('f', 'm') : Stats(),
            ('m', 'f') : Stats(),
            ('m', 'm') : Stats(),
        }
    def bucket(self, expected, stereotype):
        return self.map[(expected, stereotype)]

if __name__ == '__main__':
    opt = argparse.ArgumentParser(description="write program description here")

    # insert options here
    opt.add_argument('src_file', type=str, help='this is a positional arg')
    opt.add_argument('expected_gender_file', type=str, help='this is a positional arg')
    opt.add_argument('dictionary', type=str, help='this is a positional arg')
    options = opt.parse_args()

    dictionary = {}
    for line in open(options.dictionary, 'r', encoding='utf-8').readlines():
        items = line.strip().split(',')
        dictionary[items[0].lower()] = {'m': items[1].lower().split('|'), 'f': items[2].lower().split('|')}

    src_lines = open(options.src_file, 'r', encoding='utf-8')
    translation_lines = io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8')
    expected_gender_lines = open(options.expected_gender_file, 'r', encoding='utf-8')
    buckets = Buckets()
    for src_line, translation_line, expected_gender in zip(src_lines, translation_lines, expected_gender_lines):
        src_line = src_line.lower().strip()
        translation_line = translation_line.lower().strip()
        expected_gender, stereotype_gender = expected_gender.strip().lower().split()
        for k in dictionary:
            k_re = re.compile(r'\b%s\b' % k, re.I)
            if k_re.search(src_line):
                f_expected_translation = dictionary[k]['f']
                m_expected_translation = dictionary[k]['m']
                found_correct_match = False
                found_wrong_match = False
                for m_exp in m_expected_translation:
                    match = re.compile(r'\b%s\b' % m_exp, re.I)
                    if match.search(translation_line):
                        if expected_gender == 'm':
                            found_correct_match = True
                        else: # expected gender == 'f'
                            found_wrong_match = True
                        break

                if not found_wrong_match and not found_correct_match:
                    for f_exp in f_expected_translation:
                        match = re.compile(r'\b%s\b' % f_exp, re.I)
                        if match.search(translation_line):
                            if expected_gender == 'm':
                                found_wrong_match = True
                            else: # expected gender == 'f'
                                found_correct_match = True
                            break
                stats = buckets.bucket(expected_gender, stereotype_gender)
                if found_correct_match and found_wrong_match:
                    stats.inconclusive += 1
                elif not found_correct_match and not found_wrong_match:
                    stats.inconclusive += 1
                elif found_correct_match:
                    stats.right += 1
                elif found_wrong_match:
                    stats.wrong += 1
    
    print("Stereotype Context Right       Wrong       Inconclusive")
    for occupation in ['f', 'm']:
        for context in ['f', 'm']:
            stats = buckets.bucket(context, occupation)
            print("{: <10s} {: <7s} {:s}".format(occupation, context, str(stats)))
    pro = buckets.bucket('f', 'f') + buckets.bucket('m', 'm')
    anti = buckets.bucket('f', 'm') + buckets.bucket('m', 'f')
    overall = pro + anti
    print("Stereotypical      " + str(pro))
    print("Anti-Stereotypical " + str(anti))
    print("Overall            " + str(overall))
    
