# https://www.hackerrank.com/challenges/py-set-mutations/problem

a_count = int(input())
a = set(map(int, input().split()))

n = int(input())

for _ in range(n):
    name, length = input().split()
    s = set(map(int, input().split()))

    if name == "intersection_update":
        a.intersection_update(s)

    elif name == "update":
        a.update(s)

    elif name == "symmetric_difference_update":
        a.symmetric_difference_update(s)

    elif name == "difference_update":
        a.difference_update(s)

print(sum(a))

