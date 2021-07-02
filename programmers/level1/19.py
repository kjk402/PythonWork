
# 19번 수박수

def solution(n):
    answer = ''
    for i in range(1, n+1):
        if i%2 == 0:        #짝수일 경우
            answer+="박"
        else:               #홀수일 경우
            answer+="수"
    return answer

n = 3
print(solution(n))