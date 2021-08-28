# https://www.hackerrank.com/challenges/py-set-union/problem

n = int(input())
english = set(input().split())

b = int(input())
french = set(input().split())

print(len(english.union(french)))

