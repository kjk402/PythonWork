# 9번 3진법 뒤집기

import math

def solution(n):
    answer = 0
    sam = []
    while n!=0:
        sam.append(n % 3)
        n = n//3

    for i in range(0,len(sam)):
        answer = answer + sam[len(sam)-1-i]*int(math.pow(3,i))
    return answer