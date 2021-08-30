# https://www.hackerrank.com/challenges/matching-one-or-more-repititions/problem

Regex_Pattern = r"^[0-9]+[A-Z]+[a-z]+$"

import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())

