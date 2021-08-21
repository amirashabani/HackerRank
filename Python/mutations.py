# https://www.hackerrank.com/challenges/python-mutations/problem

def mutate_string(string, position, character):
    before = string[:int(position)]
    after = string[int(position)+1:]
    return f"{before}{character}{after}"

if __name__ == "__main__":
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)

