# https://www.hackerrank.com/challenges/itertools-combinations-with-replacement/problem
from itertools import combinations_with_replacement as cwr

s, k = input().split()

for c in cwr(sorted(s), int(k)):
    print(''.join(c))

