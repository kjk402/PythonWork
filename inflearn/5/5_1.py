# 5-1 가증 큰 수
# 숫자 하나 주어지고 m 개의 숫자를 제거하여 가장 큰 수 만들기

import sys
sys.stdin = open("input.txt", "rt", encoding='utf8')

n, m = map(int, input().split())

n = list(map(int, str(n)))

stack = []
for x in n:
    while stack and m>0 and stack[-1]<x:
        stack.pop()
        m -=1
    stack.append(x)
if m != 0:
    stack = stack[:-m]

for a in stack:
    print(a, end='')


"""
5276823 3

9977252641 5
"""