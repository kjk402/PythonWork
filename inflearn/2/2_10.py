# 2-10 점수 계산

# OX 문제에서 맞으면 1점 틀리면 0점
# 조건 1 => 연속으로 맞으면 가산점 준다 1 2 3

import sys
sys.stdin = open("input.txt", "rt", encoding="utf8")

n = int(input())
a = list(map(int, input().split()))

sum = 0
cnt = 0 # 가산점

for x in a:
    print(x, end=' ')
    if x==1:
        cnt +=1
        sum +=cnt
    else:
        cnt = 0

print(sum)

"""
10
1 0 1 1 1 0 0 1 1 0
"""