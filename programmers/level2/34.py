#34 최소공배수


def solution(arr):
    answer = 0
    # 1. 최대공약수를 구하는 함수
    def getGcd(a, b):
        c = max(a, b)
        d = min(a, b)

        while True:
            if c % d == 0:
                break
            c, d = d, c % d
        return d

    # 2. 최소공배수를 구하는 함수
    def getLcm(a, b):
        return a * b // getGcd(a, b)

    while True:
        arr.append(getLcm(arr.pop(), arr.pop()))  # 3. 함수 적용시키며 하나로 모아주기!
        if len(arr) == 1:  # 하나일 때 break!
            break

    answer = arr[0]

    return answer

a = [2,6,8,14]
print(solution(a))

"""
import math
def solution(num):
    answer = num[0]
    for n in num:
        answer = (n*answer) // math.gcd(n,answer)
    return answer
"""