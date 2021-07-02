# 5-5 공주 구하기 (큐)

from collections import *

import sys
sys.stdin = open("input.txt", "rt", encoding='utf8')

n, k = map(int, input().split())

dq = list(range(1,n+1))
dq = deque(dq)

while dq:
    for _ in range(k-1):
        man = dq.popleft()
        dq.append(man)
    dq.popleft()
    if len(dq)==1:
        print(dq[0])
        dq.popleft()

"""
8 3
"""