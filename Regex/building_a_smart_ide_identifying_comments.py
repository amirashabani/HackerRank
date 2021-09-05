# https://www.hackerrank.com/challenges/ide-identifying-comments/problem

import re
import sys

pattern = r"((?:\/\*(?:(?:.|\n)*?)\*\/)|(?:\/\/.*))"

text = sys.stdin.read()

match = re.findall(pattern, text)

for m in match:
    if '\n' in m:
        print('\n'.join([x.lstrip() for x in m.split('\n')]))
    else:
        print(m)

