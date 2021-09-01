# https://www.hackerrank.com/challenges/hackerrank-tweets/problem

import re

pattern = r"hackerrank"

n = int(input())

count = 0
for _ in range(n):
    line = input()
    match = re.search(pattern, line, re.I)
    if match:
        count += 1

print(count)

