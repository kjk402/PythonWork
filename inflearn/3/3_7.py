# 3-7 사과나무

# N이 주어지면
# N*N 격자판 생김
# 그리고 자연수 주어진다.
# 다이아몬드로 모양 그려서 합산


import sys
sys.stdin = open("../4/input.txt", "rt")
n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]

answer = 0
s=e = n//2
for i in range(n):
    for j in range(s, e+1):
        answer += a[i][j]
    if i<n//2:
        s -= 1
        e += 1
    else:
        s += 1
        e -= 1
print(answer)


#
# 5
# 10 13 10 12 15
# 12 39 30 23 11
# 11 25 50 53 15
# 19 27 29 37 27
# 19 13 30 13 19