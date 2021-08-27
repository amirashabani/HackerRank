# https://www.hackerrank.com/challenges/any-or-all/problem

_, line = input(), input().split()
print(all([int(x) > 0 for x in line]) and any([x == x[::-1] for x in line]))

