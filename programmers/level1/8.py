# 8번 가운데 글자 가져오기


def solution(s):
    answer =''
    if len(s) %2==0:
        answer = s[len(s)//2-1: len(s)//2+1]
    else:
        answer = s[len(s)//2]

    return answer

s = "abcde"
print(solution(s))