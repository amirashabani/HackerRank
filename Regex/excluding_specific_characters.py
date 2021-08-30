# https://www.hackerrank.com/challenges/excluding-specific-characters/problem

Regex_Pattern = r"^[\D][^aeiou][^bcDF][^ \t\r\f\n][^AEIOU][^\.,]$"

import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())

