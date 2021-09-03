# https://www.hackerrank.com/challenges/uk-and-us/problem

import re

n = int(input())
sentences = [input() for _ in range(n)]

t = int(input())

for _ in range(t):
    count = 0
    word = input()[:-2]
    pattern = r"{}(ze|se)".format(word)
    for s in sentences:
        match = re.findall(pattern, s)
        count += len(match)

    print(count)

