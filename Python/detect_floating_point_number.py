# https://www.hackerrank.com/challenges/introduction-to-regex/problem

n = int(input())

for _ in range(n):
    string = input()
    if string[-1] == '.':
        string = string[:-1]
    try:
        int(string)
        print("False")
    except:
        try:
            float(string)
            print("True")
        except:
            print("False")

