# https://www.hackerrank.com/challenges/itertools-product/problem
from itertools import product

a = map(int, input().split())
b = map(int, input().split())

print(' '.join([str(x) for x in product(a, b)]))

