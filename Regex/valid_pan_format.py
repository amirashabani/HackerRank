# https://www.hackerrank.com/challenges/valid-pan-format/problem

import re

pattern = r"^[A-Z]{5}[0-9]{4}[A-Z]$"

n = int(input())

for _ in range(n):
    line = input()
    match = re.match(pattern, line)
    if match:
        print("YES")
    else:
        print("NO")

