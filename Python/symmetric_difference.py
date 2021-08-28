# https://www.hackerrank.com/challenges/symmetric-difference/problem

m = int(input())
m_set = set(map(int, input().split()))

n = int(input())
n_set = set(map(int, input().split()))

union = m_set.union(n_set)
intersection = m_set.intersection(n_set)
symmetric_difference = union.difference(intersection)

print('\n'.join([str(x) for x in sorted(symmetric_difference)]))

