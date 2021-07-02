# 12번 두정수 사의의 합

def solution(a, b):
    l = max(a, b)
    s = min(a,b)
    answer =0
    for i in range(s, l+1):
        answer += int(i)

    return answer

a = 5
b= 3
print(solution(a, b))