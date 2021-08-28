# https://www.hackerrank.com/challenges/py-collections-deque/problem
from collections import deque

n, d = int(input()), deque()

for _ in range(n):
    command = input().split()

    if command[0] == "append":
        d.append(command[1])

    elif command[0] == "appendleft":
        d.appendleft(command[1])

    elif command[0] == "pop":
        d.pop()

    elif command[0] == "popleft":
        d.popleft()

print(' '.join(d))

