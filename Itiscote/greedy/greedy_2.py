# 큰수의 법칙

n, m, k = map(int, input().split())
data = list(map(int, input().split()))


data.sort()
print(data)

first = data[n-1]
second = data[n-2]

result = 0

while True:
    for i in range(k):
        if m==0:
            break
        result += first
        m -=1
    if m==0:
        break
    result += second
    m -=1

print(result)

"""
5 8 3
2 4 5 4 6

5 7 2 
3 4 3 4 3

"""