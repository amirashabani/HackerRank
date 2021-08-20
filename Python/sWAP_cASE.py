# https://www.hackerrank.com/challenges/swap-case/problem

def swap_case(s):
    result = ''
    for letter in s:
        if letter.upper() == letter:
            result += letter.lower()
        else:
            result += letter.upper()
    return result

if __name__ == "__main__":
    s = input()
    result = swap_case(s)
    print(result)

