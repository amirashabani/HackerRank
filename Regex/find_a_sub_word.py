# https://www.hackerrank.com/challenges/find-substring/problem
import re

n = int(input())
sentences = [input() for _ in range(n)]
q = int(input())

for _ in range(q):
    count = 0
    line = input()
    pattern = r"(?=\w({})\w)".format(line)
    for s in sentences:
        count += len(re.findall(pattern, s))

    print(count)
