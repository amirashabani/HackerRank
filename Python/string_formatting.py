# https://www.hackerrank.com/challenges/python-string-formatting/problem

def print_formatted(number):
    for i in range(1, number+1):
        length = len(f"{number:b}")
        binary = f"{i:b}".rjust(length)
        decimal = f"{i}".rjust(length)
        octal = f"{i:o}".rjust(length)
        hexadecimal = f"{i:x}".upper().rjust(length)
        print(decimal, octal, hexadecimal, binary)


if __name__ == "__main__":
    n = int(input())
    print_formatted(n)

