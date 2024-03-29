#!/usr/bin/env python3

"""Process a file by word lenth using defaultdict(int).

Use a dict to track how many words of each length are in the file.
That is, how many three-letter words, four-letter words, five-letter words, and so on.
Display your results.
"""

import os
from collections import defaultdict

words_db = defaultdict(int)

file = "words.log"
cmd = os.getcwd()

with open(f"{cmd}/dicts/{file}") as f_reader:
    lines = f_reader.readlines()
    for line in lines:
        words_in_line = line.strip().split()
        for word in words_in_line:
            words_db[len(word)] += 1

for k, v in words_db.items():
    print(f"word length of {k} has occurrences {v}")
