# https://www.hackerrank.com/challenges/collections-counter/problem

shoes_count = int(input())
sizes = input().split()
customers_count = int(input())
earned = 0

for i in range(customers_count):
    shoe, price = input().split()
    if shoe in sizes:
        earned += int(price)
        sizes.remove(shoe)

print(earned)

