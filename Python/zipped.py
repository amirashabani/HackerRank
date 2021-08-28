# https://www.hackerrank.com/challenges/zipped/problem

n, x = map(int, input().split())

scores = []
for _ in range(x):
    scores.append(list(map(float, input().split())))

for student in zip(*scores):
    print(sum(student) / x)

