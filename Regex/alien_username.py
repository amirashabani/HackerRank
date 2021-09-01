# https://www.hackerrank.com/challenges/alien-username/problem

import re

pattern = r"^[_.][0-9]+[a-zA-Z]*_?$"

n = int(input())

for _ in range(n):
    line = input()
    match = re.match(pattern, line)
    if match:
        print("VALID")
    else:
        print("INVALID")

