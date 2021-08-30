# https://www.hackerrank.com/challenges/backreferences-to-failed-groups/problem

Regex_Pattern = r"^[0-9]{2}(\-?)[0-9]{2}\1[0-9]{2}\1[0-9]{2}$"

import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())

