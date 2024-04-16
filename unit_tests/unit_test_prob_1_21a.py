#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
import sys
from automata.fa.nfa import NFA
import re

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

### Open files and populate lists ###
accept_file = open("unit_tests/inputs/1_21a_accepts.txt", "r")
reject_file = open("unit_tests/inputs/1_21a_rejects.txt", "r")
accept_list = accept_file.readlines()
reject_list = reject_file.readlines()

### Remove newlines ###
for i in range(len(accept_list)):
    accept_list[i] = accept_list[i][:-1]
for i in range(len(reject_list)):
    reject_list[i] = reject_list[i][:-1]

### Test Inputs ###
from prob_1_21a import prob_1_21a
test_machine = NFA.from_regex(prob_1_21a, input_symbols={'a', 'b'})

UNEXPECTED = []

for w in accept_list:
    if (w not in test_machine):
        UNEXPECTED.append(w)

for w in reject_list:
    if (w in test_machine):
        UNEXPECTED.append(w)

### Not Allowing automata-lib Functions ###
pattern = "accepts_input|copy|read_input|read_input_stepwise|validate|iter_transitions|show_diagram|cardinality|clear_cache|complement|count_mod|count_words_of_length|difference|empty_language|from_finite_language|from_nfa|from_prefix|from_subsequence|from_substring|from_substrings|from_suffix|intersection|isdisjoint|isempty|isfinite|issubset|issuperset|iter_transitions|maximum_word_length|minify|minimum_word_length|nth_from_end|nth_from_start|of_length|predecessor|predecessors|random_word|read_input_stepwise|successor|successors|symmetric_difference|to_complete|to_partial|union|universal_language|validate|words_of_length|concatenate|edit_distance|eliminate_lambda|from_dfa|from_regex|intersection|iter_transitions|kleene_star|left_quotient|option|read_input_stepwise|reverse|right_quotient|shuffle_product|union|validate|from_dfa|from_nfa|iter_transitions|to_regex|validate|isequal|issubset|issuperset|validate"
with open("prob_1_21a.py","r") as file:
    for line in file:
        if re.search(pattern, line):
            print("automata-lib funcs not allowed for this assignment")
            print(f"-->{line[:-1]}")
            sys.exit(1)

if len(UNEXPECTED) > 0:
    print("UNEXPECTED RESULT ON THESE INPUTS: ", end="")
    if len(UNEXPECTED) > 10:
        print("[", end="")
        for i in range(9):
            print(f"\'{UNEXPECTED[i]}\'", end=", ")
        print(f"\'{UNEXPECTED[9]}\', ...]")
    else:
        print(UNEXPECTED)
    sys.exit(1)

### Clean up ###
accept_file.close()
reject_file.close()
