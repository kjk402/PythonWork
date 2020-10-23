# # 3-5 수들의 합
# N 개의 수로 된 수열
# i 부터 jㄲ 까지의 합이 m이되는 경우의 수

import sys
sys.stdin = open("../4/input.txt", "rt")

n, m = map(int, input().split())
a = list(map(int, input().split()))
lt = 0
rt = 1
tot = a[0]
cnt = 0
while True:
    if tot < m:
        if rt < n:
            tot += a[rt]
            rt += 1
        else:
            break
    elif tot == m:
        cnt += 1
        tot -=a[lt]
        lt += 1
    else:  #tot > m
        tot -= a[lt]
        lt += 1
print(cnt)

#
# 8 3
# 1 2 1 3 1 1 1 2



