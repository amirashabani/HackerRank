# https://www.hackerrank.com/challenges/detect-html-tags/problem
import re

pattern = r"<\/?\s*(?P<name>[^<>\s\/]+)[^<>]*>"
tags = set()
n = int(input())

for _ in range(n):
    line = input().strip()
    match = re.finditer(pattern, line)
    if match:
        for m in match:
            tags.add(m.group("name"))

print(';'.join(sorted(tags)))

