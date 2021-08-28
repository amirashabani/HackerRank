# https://www.hackerrank.com/challenges/py-set-symmetric-difference-operation/problem

n = int(input())
english = set(input().split())

b = int(input())
french = set(input().split())

print(len(english.symmetric_difference(french)))

