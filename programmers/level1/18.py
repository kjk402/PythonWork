# 18 소수찾기

def solution(n):
    answer =[]

    for i in range(2, n+1):
        for j in range(2,i):
            if i %j !=0:
                answer.append(i)

    return len(answer)