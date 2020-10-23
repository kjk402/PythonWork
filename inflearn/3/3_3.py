# 3-3 카드 역배치

# 1 부터 20까지 카드 주어진다
# a,b 라는 구간이 주어진다면 a 부터b까지는 역순으로 재배치
# 5,10 이면 10 9 8 7 6 5 로 재배치

# 10개의 구간이 주어진다. 최종 카드 출력력


import sys
sys.stdin = open("../4/input.txt", "rt")

arr = list(range(21))
print(arr)
for _ in range(10):
    a, b = map(int, input().split())
    for i in range((b-a+1)//2):
        arr[a+i], arr[b-i] = arr[b-i], arr[a+i]
arr.pop(0)
print(arr)
for x in arr:
    print(x, end=' ')
#
# 5 10
# 9 13
# 1 2
# 3 4
# 5 6
# 1 2
# 3 4
# 5 6
# 1 20
# 1 20





















































