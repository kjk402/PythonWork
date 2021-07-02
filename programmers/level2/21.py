# 21번 숫자의 표현

def solution(n):

    answer = 0

    for i in range(1, n + 1):
        sum = 0
        for j in range(i, n + 1):
              sum = sum + j
              if sum == n:
                answer = answer + 1
                break

              if sum > n:
                break

    return answer

n = 15
print(solution(n))