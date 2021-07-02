# 문자열 내림차순 정렬

def solution(s):

    return ''.join(sorted(s, reverse=True))


s ="Zbcdefg"

print(solution(s))