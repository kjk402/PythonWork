# 5-6 응급실

# N먕의 환자가 있다. M 번째 환자는 언제 치료 받을지
from collections import deque
import sys
sys.stdin = open("input.txt", "rt", encoding='utf8')

n, m = map(int, input().split())
a = [(pos, val) for pos, val in enumerate (list(map(int, input().split())))]

print(a)
a = deque(a)
cnt=0
print(a)
while True:
    man = a.popleft()
    if any(man[1]<x[1] for x in a):
        a.append(man)
    else:
        cnt +=1
        if man[0] == m:
            print(cnt)
            break