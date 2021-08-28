# https://www.hackerrank.com/challenges/py-collections-ordereddict/problem
from collections import OrderedDict

items = OrderedDict()

n = int(input())
for _ in range(n):
    item, price = input().rsplit(' ', 1)
    if item in items:
        items[item] += int(price)
    else:
        items[item] = int(price)

for item in items:
    print(item, items[item])

