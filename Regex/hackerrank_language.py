# https://www.hackerrank.com/challenges/hackerrank-language/problem

import re

pattern = (
    r"^\d+ (C|CPP|JAVA|PYTHON|PERL|PHP|RUBY|CSHARP"
    r"|HASKELL|CLOJURE|BASH|SCALA|ERLANG|CLISP"
    r"|LUA|BRAINFUCK|JAVASCRIPT|GO|D|OCAML|R"
    r"|PASCAL|SBCL|DART|GROOVY|OBJECTIVEC)$"
)

n = int(input())

for _ in range(n):
    line = input()
    match = re.match(pattern, line)
    if match:
        print("VALID")
    else:
        print("INVALID")

