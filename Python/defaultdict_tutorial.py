# https://www.hackerrank.com/challenges/defaultdict-tutorial/problem


n, m = list(map(int, input().split()))
a = []

for _ in range(n):
    a.append(input())

for _ in range(m):
    indices = []
    element = input()
    for i in range(n):
        if a[i] == element:
            indices.append(str(i+1))

    if len(indices) > 0:
        print(' '.join(indices))
    else:
        print("-1")

