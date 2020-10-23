# 2-6 자릿수의 합

# import sys
# sys.stdin = open("input.txt", "rt", encoding="utf8")

n = int(input())
a = list(map(int, input().split()))

def digit_sum(n):
    sum=0
    while n>0:
        sum+=n%10
        n=n//10
    return sum

max = -2147000000
for x in a:
    print(x, end=' ')
    total = digit_sum(x)
    if total >max:
        max=total
        ans=x
print(ans, total)