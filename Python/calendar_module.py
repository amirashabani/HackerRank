# https://www.hackerrank.com/challenges/calendar-module/problem

import calendar
from datetime import datetime

string = input()
date = datetime.strptime(string, "%m %d %Y")
day = calendar.day_name[date.weekday()]

print(day.upper())

