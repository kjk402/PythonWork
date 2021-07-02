# 5-4 후위 연산 계산하기

import sys
sys.stdin = open("input.txt", "rt", encoding='utf8')


a = input()

stack = []


for x in a:
    if x.isdecimal():
        stack.append(int(x))
    elif x =='+':
        n1 = stack.pop()
        n2 = stack.pop()
        stack.append(n2 + n1)
    elif x =='-':
        n1 = stack.pop()
        n2 = stack.pop()
        stack.append(n2 - n1)
    elif x=='*':
        n1 = stack.pop()
        n2 = stack.pop()
        stack.append(n2 * n1)
    elif x=='/':
        n1 = stack.pop()
        n2 = stack.pop()
        stack.append(n2 / n1)

# for x in stack:
#     print(x)
print(stack[0])



"""
352+*9-
"""