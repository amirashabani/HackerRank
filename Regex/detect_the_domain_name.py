# https://www.hackerrank.com/challenges/detect-the-domain-name/problem

import re

pattern = r"(?:https?:\/\/)(?:ww(?:w|\d+)\.)?((?:(?:[\w-]+\.)+)(?:[a-zA-Z0-9]{2,}))"

n = int(input())
urls = set()

for _ in range(n):
    line = input()
    match = re.finditer(pattern, line)
    if match:
        for m in match:
            urls.add(m.group(1))

print(';'.join(sorted(urls)))

