# https://www.hackerrank.com/challenges/validating-uid/problem

n = int(input())

for _ in range(n):
    uid = input()

    if len(uid) != 10 or not uid.isalnum():
        print("Invalid")
    else:
        uppercases = 0
        digits = 0
        for letter in uid:
            if letter.isupper():
                uppercases += 1
            elif letter.isdigit():
                digits += 1
        if len(set(uid)) == 10 and uppercases >= 2 and digits >= 3:
            print("Valid")
        else:
            print("Invalid")

