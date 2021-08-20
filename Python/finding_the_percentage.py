# https://www.hackerrank.com/challenges/finding-the-percentage/problem

n = int(input())
students = {}

for _ in range(n):
    line = input().split()
    students[line[0]] = map(float, line[1:])

scores = list(students[input()])
average = sum(scores) / len(scores)
print(f"{average:.2f}")

