
# import sys
# sys.stdin = open("input.txt", "rt")

n, m = map(int, input().split())
a = list(map(int, input().split()))

a.sort()

# cnt = 0
# for i in range(n):
#     if a[i] != m:
#         cnt +=1
#     else:
#         print(cnt+1)
#         break

lt=0
rt=n-1
while lt<=rt:
    mid = (lt+rt)//2
    if a[mid] == m:
        print(mid+1)
        break
    elif a[mid] > m:
        rt = mid-1
    elif a[mid] < m:
        lt = mid+1


"""
8 32
23 87 65 12 57 32 99 81
"""