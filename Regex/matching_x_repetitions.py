# https://www.hackerrank.com/challenges/matching-x-repetitions/problem

Regex_Pattern = r"^[a-zA-Z02468]{40}[13579 \t\r\f\n]{5}$"

import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())

