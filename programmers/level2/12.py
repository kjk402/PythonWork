# 12 번 주식가격

def solution(prices):
    answer = []
    for i in range(0, len(prices)-1):
        cnt = 0
        for j in range(i+1, len(prices)):
            if prices[i] <= prices[j]:
                cnt += 1
            else:
                cnt += 1
                break
        answer.append(cnt)
    answer.append(0)
    return answer

p = [1,2,3,2,3]

print(solution(p))