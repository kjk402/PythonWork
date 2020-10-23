def solution(phone):
    answer=""
    for i in range(0, len(phone)-4):
        answer += "*"
    return answer + phone[len(phone)-4:]

num = input()
print(solution(num))