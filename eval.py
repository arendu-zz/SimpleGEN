#!/usr/bin/env python
# coding: utf-8
__author__ = 'adirendu'

import argparse
import re

if __name__ == '__main__':
    opt = argparse.ArgumentParser(description="write program description here")

    # insert options here
    opt.add_argument('src_file', type=str, help='this is a positional arg')
    opt.add_argument('expected_gender_file', type=str, help='this is a positional arg')
    opt.add_argument('translation_file', type=str, help='this is a positional arg')
    opt.add_argument('dictionary', type=str, help='this is a positional arg')
    options = opt.parse_args()

    dictionary = {}
    for line in open(options.dictionary, 'r', encoding='utf-8').readlines():
        items = line.strip().split(',')
        dictionary[items[0].lower()] = {'m': items[1].lower().split('|'), 'f': items[2].lower().split('|')}

    src_lines = open(options.src_file, 'r', encoding='utf-8').readlines()
    translation_lines = open(options.translation_file, 'r', encoding='utf-8').readlines()
    expected_gender_lines = open(options.expected_gender_file, 'r', encoding='utf-8').readlines()
    correct = 0
    wrong = 0
    inconclusive = 0
    for src_line, translation_line, expected_gender in zip(src_lines, translation_lines, expected_gender_lines):
        src_line = src_line.lower().strip()
        translation_line = translation_line.lower().strip()
        expected_gender = expected_gender.strip().lower().split()[0]
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
                if found_correct_match and found_wrong_match:
                    inconclusive += 1.0
                elif not found_correct_match and not found_wrong_match:
                    inconclusive += 1.0
                elif found_correct_match:
                    correct += 1.0
                elif found_wrong_match:
                    wrong += 1.0
    total = correct + inconclusive + wrong
    print(f"correct: {correct}, inconclusive: {inconclusive}, wrong: {wrong}")
    print(f"correct%: {correct/total}, inconclusive%: {inconclusive/total}, wrong%: {wrong/total}")
