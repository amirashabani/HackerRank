# https://www.hackerrank.com/challenges/capitalize/problem

import re
string = input()

result = re.sub(
    r"(\w+)",
    lambda m: m.group(1).capitalize(),
    string,
)
print(result)

