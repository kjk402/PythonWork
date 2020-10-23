# 3-8 모래시계 + 옮기기

# 만약 회전명령 정보가 2 0 3이면 2번째 행을 왼쪽으로 3만큼 아래 그림처럼 회전시키는 명령
# 입니다.
import sys
sys.stdin = open("../4/input.txt", "rt")
n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
m = int(input())
for i in range(m):
    h, t, k = map(int, input().split())
    if t==0:
        for _ in range(k):
            a[h-1].append(a[h-1].pop(0))
    else:
        for _ in range(k):
            a[h-1].insert(0, a[h-1].pop())

answer = 0
s = 0
e = n-1
for i in range(n):
    for j in range(s, e+1):
        answer += a[i][j]
    if i < n//2:
        s +=1
        e -=1
    else:
        s -=1
        e +=1
print(answer)





#
#
# 5
# 10 13 10 12 15
# 12 39 30 23 11
# 11 25 50 53 15
# 19 27 29 37 27
# 19 13 30 13 19
# 3
# 2 0 3
# 5 1 2
# 3 1 4





