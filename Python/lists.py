# https://www.hackerrank.com/challenges/python-lists/problem

n = int(input())

l = []
for _ in range(n):
    line = input().split()
    if line[0] == "insert":
        l.insert(int(line[1]), int(line[2]))
    elif line[0] == "print":
        print(l)
    elif line[0] == "remove":
        l.remove(int(line[1]))
    elif line[0] == "append":
        l.append(int(line[1]))
    elif line[0] == "sort":
        l = sorted(l)
    elif line[0] == "pop":
        l.pop()
    elif line[0] == "reverse":
        l.reverse()

