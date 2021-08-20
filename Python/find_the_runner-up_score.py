# https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem

n = int(input())
scores = sorted(set(map(int, input().split())))

if len(scores) == 1:
    print(scores[0])
else:
    print(scores[-2])

