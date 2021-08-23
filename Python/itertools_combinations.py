# https://www.hackerrank.com/challenges/itertools-combinations/problem

from itertools import combinations

string, k = input().split()

for i in range(1, int(k)+1):
    for c in combinations(sorted(string), i):
        print(''.join(c))

