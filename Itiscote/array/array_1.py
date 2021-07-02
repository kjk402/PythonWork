
n = int(input())
a = []

for _ in range(n):
    a.append(int(input()))

a.sort(reverse=True)

for x in a:
    print(x, end=' ')

"""
3
15
27
12
"""