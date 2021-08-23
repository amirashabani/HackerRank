# https://www.hackerrank.com/challenges/the-minion-game/problem

def minion_game(string):
    vowels = "AEIOU"
    kevin = stuart = 0
    length = len(string)

    for i in range(length):
        if string[i] in vowels:
            kevin += (length - i)
        else:
            stuart += (length - i)

    if kevin == stuart:
        print("Draw")
    elif kevin > stuart:
        print("Kevin", kevin)
    else:
        print("Stuart", stuart)


if __name__ == "__main__":
    s = input()
    minion_game(s)

