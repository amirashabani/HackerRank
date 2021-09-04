# https://www.hackerrank.com/challenges/find-a-word/problem

import re

n = int(input())
sentences = [input() for _ in range(n)]
t = int(input())

for _ in range(t):
    line = input()
    pattern = r"\b{}\b".format(line)
    count = 0
    for s in sentences:
        match = re.findall(pattern, s)
        count += len(match)

    print(count)

