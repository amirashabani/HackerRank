# https://www.hackerrank.com/challenges/utopian-identification-number/problem

import re

pattern = r"^[a-z]{,3}[0-9]{2,8}[A-Z]{3,}$"
n = int(input())

for _ in range(n):
    line = input()
    match = re.match(pattern, line)
    if match:
        print("VALID")
    else:
        print("INVALID")

