# https://www.hackerrank.com/challenges/re-findall-re-finditer/problem

import re

pattern = r"(?<=[^aeiou])([aeiou]{2,})(?=[^aeiou])"
match = re.findall(pattern, input(), re.I)

if match:
    for item in match:
        print(item)
else:
    print(-1)

