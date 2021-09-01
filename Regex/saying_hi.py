# https://www.hackerrank.com/challenges/saying-hi/problem

import re

pattern = r"^[Hh][Ii]\s[^Dd].*$"

n = int(input())

for _ in range(n):
    line = input()
    match = re.search(pattern, line)
    if match:
        print(line)

