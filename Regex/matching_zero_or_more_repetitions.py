# https://www.hackerrank.com/challenges/matching-zero-or-more-repetitions/problem

Regex_Pattern = r"^[0-9]{2,}[a-z]*[A-Z]*$"

import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())

