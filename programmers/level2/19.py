# 19번 올바른 괄호
"""
s = input()
stack = []
cnt = 0
for i in range(len(s)):
    if s[i]=='(' :
        stack.append(s[i])
    else:
        if s[i-1] == '(' : #바로 앞이 닫는 것이면 레이저임 ()
            stack.pop()
            cnt += len(stack)
        else:
            stack.pop()
            cnt +=1

print(cnt)

"""


def solution(s):
    answer = True
    stack = []
    if s[0] == ')':
        return False
    for x in s:
        if x=='(':
            stack.append('(')
        else:
            try: stack.pop()
            except: return False
    if len(stack) == 0:
        return True
    else:
        return False




s="()()"
print(solution(s))