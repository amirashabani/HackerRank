# https://www.hackerrank.com/challenges/programming-language-detection/problem

import sys

text = sys.stdin.read()

if "import java" in text:
    print("Java")
elif "int main" in text:
    print("C")
else:
    print("Python")

