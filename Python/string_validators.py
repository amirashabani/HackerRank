# https://www.hackerrank.com/challenges/string-validators/problem

line = input()

print(any([x.isalnum() for x in line]))
print(any([x.isalpha() for x in line]))
print(any([x.isdigit() for x in line]))
print(any([x.islower() for x in line]))
print(any([x.isupper() for x in line]))

