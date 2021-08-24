# https://www.hackerrank.com/challenges/polar-coordinates/problem

from cmath import phase

number = complex(input())

print(abs(number))
print(phase(number))

