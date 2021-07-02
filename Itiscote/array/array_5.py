# 5 안테나
n = int(input())

a = list(map(int, input().split()))
a.sort()


print(a[(n-1)//2])


"""
4
5 1 7 9 
"""