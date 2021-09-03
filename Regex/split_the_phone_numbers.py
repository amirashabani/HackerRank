# https://www.hackerrank.com/challenges/split-number/problem

import re

pattern = r"^(\d{1,3})([- ])(\d{1,3})\2(\d{4,10})$"

n = int(input())

for _ in range(n):
    line = input()
    match = re.match(pattern, line)
    if match:
        result = (
            f"CountryCode={match.group(1)},"
            f"LocalAreaCode={match.group(3)},"
            f"Number={match.group(4)}"
        )
        print(result)

