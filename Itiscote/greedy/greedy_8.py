# 8 만들수 없는 금액

n = int(input())
coin = list(map(int, input().split()))
coin.sort()

print(coin)

result = 1

for x in coin:
    if result < x:
        break
    else:
        result += x
print(result)


"""
5
3 2 1 1 9

"""