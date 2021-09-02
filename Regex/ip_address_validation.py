# https://www.hackerrank.com/challenges/ip-address-validation/problem

import re

ipv4_pattern = (
    r"^(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.){3}"
    r"([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])$"
)

ipv6_pattern = r"^(([0-9a-fA-F]{1,4}):){7}([0-9a-fA-F]{1,4})$"

n = int(input())

for _ in range(n):
    line = input().strip()
    ipv4 = re.match(ipv4_pattern, line)
    ipv6 = re.match(ipv6_pattern, line)
    if ipv4:
        print("IPv4")
    elif ipv6:
        print("IPv6")
    else:
        print("Neither")

