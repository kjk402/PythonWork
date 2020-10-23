# 4-3
# n개의 곡을 담는 M개의 dvd
# dvd의 용량은 모두 같을 때 용량의 최소를 구하기.

import sys
sys.stdin = open("input.txt", "rt")
def Count(cap):
    cnt=1
    sum=0
    for x in a:
        if sum+x>cap:
            cnt +=1
            sum = x
        else:
            sum+=x
    return cnt
n, m = map(int, input().split())
a = list(map(int, input().split()))

lt=1
rt=sum(a)
res=0
while lt<=rt:
    mid = (lt+rt)//2
    if Count(mid)<=m:
        res = mid
        rt = mid-1
    else: #용량이 작아서 더 큰 용량 필요
        lt = mid +1
print(res)



"""
9 3
1 2 3 4 5 6 7 8 9
"""