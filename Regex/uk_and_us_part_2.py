# https://www.hackerrank.com/challenges/uk-and-us-2/problem
import re

n = int(input())
sentences = [input() for _ in range(n)]

t = int(input())

for _ in range(t):
    uk = input()
    us = uk.replace("our", "or")
    pattern = r"(\b{}\b|\b{}\b)".format(uk, us)

    count = 0
    for s in sentences:
        match = re.findall(pattern, s)
        count += len(match)

    print(count)

