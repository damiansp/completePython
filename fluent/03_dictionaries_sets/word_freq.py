# Index mapping word -> list of occurrences
import collections
import re
import sys

WORD_RE = re.compile('\w+')
index = {} 

with open(sys.argv[1], encoding='utf-8') as fp:
    for line_no, line in enumerate(fp, 1):
        for match in WORD_RE.finditer(line):
            word = match.group()
            column_no = match.start() + 1
            location = (line_no, column_no)

            # Bad way:
            #occurrences = index.get(word, [])
            #occurrences.append(location)
            #index[word] = occurrences

            # Good way:
            index.setdefault(word, []).append(location)

# print in alphabetical order
for word in sorted(index, key=str.upper):
    print(word, index[word])


    

# Alternately
index = collections.defaultdict(list)
with open(sys.argv[1], encoding='utf-8') as fp:
    for line_no, line in enumerate(fp, 1):
        for match in WORD_RE.finditer(line):
            word = match.group()
            column_no = match.start() + 1
            location = (line_no, column_no)
            
            index[word].append(location)

            
# print in alphabetical order
for word in sorted(index, key=str.upper):
    print(word, index[word])
