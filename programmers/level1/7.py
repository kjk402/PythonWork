# 7번 2016년

def solution(a, b):
    answer = ["THU", "FRI", "SAT", "SUN", "MON", "TUE", "WED"]
    month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    day = sum(month[:a - 1]) + b if a > 1 else b

    return answer[day % 7]

import datetime

def getDayName(a,b):
    t = 'MON TUE WED THU FRI SAT SUN'.split()
    return t[datetime.datetime(2016, a, b).weekday()]

a = 5
b = 24
print(solution(a, b))
print(getDayName(a, b))