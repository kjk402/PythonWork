# 곱하기 혹은 더하기

n = input()
print(n)

result = int(n[0])
for i in range(1, len(n)):
    num = int(n[i])
    if result <=1 or num <=1:
        result +=num
    else:
        result *=num

print(result)

"""
02984
"""