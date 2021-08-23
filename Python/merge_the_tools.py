# https://www.hackerrank.com/challenges/merge-the-tools/problem

def merge_the_tools(string, k):
    subs = [string[i:i+k] for i in range(0, len(string), k)]
    for sub in subs:
        unique = []
        for letter in sub:
            if letter not in unique:
                unique.append(letter)
        print(''.join(unique))



if __name__ == "__main__":
    string, k = input(), int(input())
    merge_the_tools(string, k)

