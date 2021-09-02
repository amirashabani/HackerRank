# https://www.hackerrank.com/challenges/detecting-valid-latitude-and-longitude/problem

import re

pattern = (
    r"\([-+]?([0-9]|[1-8][0-9]|90)(\.\d+)?, "
    r"[-+]?(180(\.0+)?|([0-9]|[1-9][0-9]|1[0-7][0-9])(\.\d+)?)\)"
)

n = int(input())

for _ in range(n):
    line = input().strip()
    match = re.match(pattern, line)
    if match:
        print("Valid")
    else:
        print("Invalid")

