# https://www.hackerrank.com/challenges/write-a-function/problem

def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            return False
        return True
    return False

if __name__ == "__main__":
    year = int(input())
    print(is_leap(year))

