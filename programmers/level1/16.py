# 16 문자열 다루기 기본

def solution(s):
    if len(s) ==4 or len(s)==6:
        if s.isdigit():
            return True

    return False


s= "1234"
print(solution(s))