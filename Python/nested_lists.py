# https://www.hackerrank.com/challenges/nested-list/problem

from collections import defaultdict

n = int(input())
students = defaultdict(list)
for _ in range(n):
    name = input()
    score = float(input())
    students[score].append(name)

scores = sorted(set(students.keys()))

if len(scores) == 1:
    print('\n'.join(sorted(students[scores[0]])))
else:
    print('\n'.join(sorted(students[scores[1]])))

