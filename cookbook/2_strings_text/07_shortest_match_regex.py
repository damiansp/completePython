import re


quote_pat = re.compile(r'\"(.*)\"')
txt = 'Computer says "no", phone says "yes"'
print(quote_pat.findall(txt))  # ['no", phone says "yes']

quote_pat_non_greedy = re.compile(r'\"(.*?)\"')
print(quote_pat_non_greedy.findall(txt))  # ['no', 'yes']

