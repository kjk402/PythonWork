n = int(input())
arrn = list(map(int, input().split()))
m = int(input())
arrm = list(map(int, input().split()))

print(arrn)
print(arrm)

arrn.extend(arrm)
# for x in arrm:
#     arrn.append(x)
arrn.sort()

for y in arrn:
    print(y, end=' ')

# 3
# 1 3 5
# 5
# 2 3 6 7 9