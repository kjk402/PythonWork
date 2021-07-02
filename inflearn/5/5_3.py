# 5-3 후위표기식 만들기

# 3+5 * 2 /(7-2) > 352*72 -/+
import sys
sys.stdin = open("input.txt", "rt", encoding='utf8')


a = input()
stack =[]
res = ''
for x in a:
    if x.isdecimal():
        res+=x
    else:
        if x=='(':
            stack.append(x)
        elif x=='*' or x=='/' :
            while stack and (stack[-1]=='*' or stack[-1]=='/'):
                res+= stack.pop()
            stack.append(x)
        elif x=='+' or x== '-':
            while stack and stack[-1] != '(': # 괄호 있으면 우선 연산 해야함
                res += stack.pop()
            stack.append(x)
        elif x==')':
            while stack and stack[-1] != '(':
                res+= stack.pop()
            stack.pop()
while stack:
    res += stack.pop()

print(res)
"""
3*(5+2)-9
"""
