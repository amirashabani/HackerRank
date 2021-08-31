# https://www.hackerrank.com/challenges/detect-html-links/problem
import re

pattern = r'<a href="(?P<link>.*?)".*?>(<[^\/]*>)*(?P<text>[^<>]*)(<.*>)*<\/a>'
n = int(input())

for _ in range(n):
    line = input().strip()
    match = re.finditer(pattern, line)
    if match:
        for m in match:
            link = m.group("link").strip()
            text = m.group("text").strip()
            print(link, ',', text, sep='')

