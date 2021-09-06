# https://www.hackerrank.com/challenges/stack-exchange-scraper/problem

import re
import sys


ids_pattern = r'"question-summary-(\d+)"'
question_pattern = r'class="question-hyperlink">(.*)<\/a>'
time_pattern = r'class="relativetime">(.*)<\/span>'

text = sys.stdin.read()

ids = re.findall(ids_pattern, text)
questions = re.findall(question_pattern, text)
relative_times = re.findall(time_pattern, text)

zipped = zip(ids, questions, relative_times)

for q in zipped:
    print(';'.join(q))

