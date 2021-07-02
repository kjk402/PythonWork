
# 14번 문자열내 p와 y 개수

def solution(s):
    s.upper()
    if s.count('P') == s.count('Y'):
        return True
    else:
        return False



s = "pPoooyY"

print(solution(s))