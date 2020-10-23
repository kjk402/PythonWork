# 4-7 창고정리
# L 이라는 창고 길이가 주어진다.
# 세로로 무작위로 박스 갯수 주어진다.
# 박스 제일 높은 곳에서 제일 낮은곳으로 높이 조정을 해야한다.
# M 번의 높이 조정 후 가장 높은 곳과 낮은 곳의 차이를 구하라.

import sys
sys.stdin = open("input.txt", "rt")

L = int(input())
a = list(map(int, input().split()))
m = int(input())

a.sort()
for _ in range(m):
    a[0] +=1
    a[L-1] -=1
    a.sort()

print((a[L-1], a[0]))
print(a[L-1] - a[0])


"""
10
69 42 68 76 40 87 14 65 76 81
50
"""