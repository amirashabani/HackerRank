# https://www.hackerrank.com/challenges/py-collections-namedtuple/problem
from collections import namedtuple
marks, n, s = 0, int(input()), namedtuple('s', input().split())
print("{:.2f}".format(sum([s(*[int(x) if x.isdigit() else x for x in input().split()]).MARKS for _ in range(n)])/n))

