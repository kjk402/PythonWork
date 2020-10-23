# 4-4 마구간 정하기
# n 개의 마구간이 있고 c개의 말이 있다.
# 좌표가 무작위로 주어질 때 c개의 말들을 마구간에 멀리 떨어트려서 두어야한다.
# 가장 가까운 두 말의 최대 거리를 출력

import sys
sys.stdin = open("input.txt", "rt")

def Count(len):
    cnt= 1
    ep=a[0]
    for i in range(1, n):
        if a[i] - ep >= len:
            cnt +=1
            ep = a[i]
    return cnt

n, c = map(int, input().split())
a=[]
for _ in range(n):
    tmp = int(input())
    a.append(tmp)
a.sort()
res = 0
lt=1
rt=a[n-1]
while lt<=rt:
    mid = (lt+rt) //2
    if Count(mid) >=c:
        res = mid
        lt=mid+1
    else:
        rt = mid -1
print(res)

"""
5 3
1
2
8
4
9
"""
