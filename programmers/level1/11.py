# 11번 나누어떨어지는 숫자 배열

def solution(arr, divisor):
    answer = []

    for x in arr:
        if x%divisor ==0:
            answer.append(x)

    answer.sort()

    if len(answer) ==0:
        answer.append(-1)

    return answer


arr= [5,9,7,10]
divi =5

print(solution(arr,divi))