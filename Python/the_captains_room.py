# https://www.hackerrank.com/challenges/py-the-captains-room/problem
from collections import Counter

k = int(input())
rooms = list(map(int, input().split()))

captain = [x for x in Counter(rooms).items() if x[1] != k]
print(captain[0][0])

