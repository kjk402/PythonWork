# 5 럭키 스트레이트

n = int(input())
left = 0
right = 0

n = list(map(int, str(n)))
print(n)

m = len(n)//2
left = sum(n[:m])
right = sum(n[m:])


if left == right:
    print("LUCKY")
else:
    print("READY")