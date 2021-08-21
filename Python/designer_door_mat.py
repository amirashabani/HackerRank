# https://www.hackerrank.com/challenges/designer-door-mat/problem

n, m = map(int, input().split())
center = (n - 1) / 2

for i in range(n):
    if i == center:
        print("WELCOME".center(m, '-'))
    else:
        pipes_count = int((abs(abs(i - center) - center) * 2) + 1)
        pipes = '..'.join(list("|" * pipes_count))
        print(f".{pipes}.".center(m, '-'))

