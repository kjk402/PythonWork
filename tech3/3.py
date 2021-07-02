# 3번

def solution(money, expected, actual):
    answer = 0
    bat = 100
    for i in range(len(expected)):
        if expected[i] == actual[i]:
            money += bat
            bat = 100
        if expected[i] != actual[i]:
            money -= bat
            if money > bat*2:
                bat *= 2
            else:
                bat = money

        if money<0:
            return 0


    return answer + money

m =1200
e = ['T', 'T', 'H', 'H', 'H']
a = ['H', 'H', 'T', 'H', 'T']

print(solution(m, e, a))