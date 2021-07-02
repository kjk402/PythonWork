#1 동전 문제

def solution(num):
    list = [50000, 10000, 5000, 1000, 500, 100, 50, 10,1]
    answer = []
    for coin in list:
        if num //coin >= 1:
            answer.append(num//coin)
            num -= (num//coin) *coin
        else:
            answer.append(0)
    return answer


n = 50237
print(solution(n))