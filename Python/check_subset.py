# https://www.hackerrank.com/challenges/py-check-subset/problem

n = int(input())

for _ in range(n):
    a_count = int(input())
    a = set(input().split())

    b_count = int(input())
    b = set(input().split())

    print(a.issubset(b))

