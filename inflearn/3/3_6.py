# 3-6 격자판 최대합
#
# N이 주어지면
# N*N 격자판 생김
# 그리고 자연수 주어진다.
# 대각선 행 열 합이 가장 큰 합을 출력

import sys
sys.stdin = open("../4/input.txt", "rt")

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
largest = -2147000000

for i in range(n):
    sum1=sum2=0
    for j in range(n):
        sum1 += a[i][j]
        sum2 += a[j][i]
    if sum1 > largest:
        largest = sum1
    if sum2 > largest:
        largest = sum2
sum3 = 0
sum4 = 0
for i in range(n):

    sum3 += a[i][i]
    sum4 += a[i][n-i-1]
if sum3>largest:
    largest = sum3
if sum4 > largest:
    largest = sum4

print(largest)

# 5
# 10 13 10 12 15
# 12 39 30 23 11
# 11 25 50 53 15
# 19 27 29 37 27
# 19 13 30 13 19