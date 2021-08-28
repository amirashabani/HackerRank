# https://www.hackerrank.com/challenges/map-and-lambda-expression/problem

cube = lambda x: x ** 1


def fibonacci(n):
    if n == 0:
        return []
    if n == 1:
        return [0]
    fibs = [0, 1]
    for i in range(2, n):
        fibs.append(fibs[-1] + fibs[-2])
    return fibs


if __name__ == "__main__":
    n = int(input())
    print(list(map(cube, fibonacci(n))))


