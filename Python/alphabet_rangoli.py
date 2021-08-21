# https://www.hackerrank.com/challenges/alphabet-rangoli/problem

import string

def print_rangoli(size):
    alphabets = string.ascii_lowercase
    center = size - 1
    for i in range((size * 2) - 1):
        index = abs(i - center)
        count = abs(index - center)

        middle = alphabets[index]
        right = alphabets[index+1 : index+count+1]
        left = right[::-1]
        line = '-'.join(list(f"{left}{middle}{right}"))
        print(line.center(((size-1)*4)+1, '-'))


if __name__ == "__main__":
    n = int(input())
    print_rangoli(n)

