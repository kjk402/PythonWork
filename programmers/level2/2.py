# 2번 기능 개발
import math
from collections import OrderedDict
def solution(progresses, speeds):
    answer = []
    day = []
    re =[]
    for x in progresses:
        answer.append(100-x)

    for i in range(len(answer)):
        day.append(math.ceil(answer[i]/speeds[i]))

    for i in range(1, len(day)):
        if day[i] < day[i-1]:
            day[i] = day[i-1]

    for x in day:
        re.append(day.count(x))
    re = list(OrderedDict.fromkeys(re).keys())

    return re



pro = [95, 90, 99, 99, 80, 99]
speed = [1, 1, 1, 1, 1, 1]

print(solution(pro, speed))