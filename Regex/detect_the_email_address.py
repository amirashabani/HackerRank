# https://www.hackerrank.com/challenges/detect-the-email-addresses/problem

import re

pattern = (
    r"([a-zA-Z_0-9_]+\.)*([a-zA-Z0-9_]+)"
    r"@([a-zA-Z_0-9_]+\.)*([a-zA-Z0-9_]+)\.([a-zA-Z]{2,})"
)

n = int(input())
emails = set()

for _ in range(n):
    line = input()
    match = re.finditer(pattern, line)
    if match:
        for m in match:
            emails.add(m.group(0))

print(';'.join(sorted(emails)))

