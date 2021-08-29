# https://www.hackerrank.com/challenges/re-group-groups/problem

import re

pattern = r"([a-zA-Z0-9])\1"
match = re.search(pattern, input())

if match:
    print(match.group(1))
else:
    print(-1)

