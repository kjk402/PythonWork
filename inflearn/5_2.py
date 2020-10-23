# 5-2  쇠막대기
# 여러 개의

import sys
sys.stdin = open("input.txt", "rt", encoding='utf8')

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
()(((()())(())()))(())
"""