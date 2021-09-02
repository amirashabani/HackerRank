# https://www.hackerrank.com/challenges/find-hackerrank/problem

import re

starts_pattern = r"^hackerrank.*$"
ends_pattern = r"^.*hackerrank$"

n = int(input())

for _ in range(n):
    line = input().strip()
    starts = re.match(starts_pattern, line)
    ends = re.match(ends_pattern, line)

    if starts and ends:
        print(0)
    elif starts:
        print(1)
    elif ends:
        print(2)
    else:
        print(-1)

