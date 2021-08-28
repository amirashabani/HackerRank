# https://www.hackerrank.com/challenges/py-check-strict-superset/problem

a = set(input().split())

n = int(input())

is_strict_superset = True
for _ in range(n):
    s = set(input().split())
    if not a.issuperset(s) or a == s:
        is_strict_superset = False

print(is_strict_superset)

