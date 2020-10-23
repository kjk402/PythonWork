
# 4-2 랜선 자르기
# k개의 랜선에서 N개의 랜선을 만든다. N개의 랜선들은 모두 길이가 같아야한다.


import sys
sys.stdin = open("input.txt", "rt")

def Count(len):
    cnt=0
    for x in Line:
        cnt += (x//len)
    return cnt

k, n = map(int, input().split())
Line = []
res = 0
largest = 0
for i in range(k):
    tmp= int(input())
    Line.append(tmp)
    largest = max(largest, tmp)
lt=1
rt=largest
while lt<=rt:
    mid = (lt+rt)//2
    if Count(mid) >= n:
        res = mid
        lt=mid+1
    else:
        rt = mid-1
print(res)



"""
4 11
802
743
457
539
"""





