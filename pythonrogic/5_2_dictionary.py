# 사전

cabinet = {3:"유재석", 100:"김태호"}

print(cabinet[100])
print(cabinet.get(3))

print(3 in cabinet)

#추가
cabinet["A-3"] = "조세호"
print(cabinet["A-3"])

#삭제
del cabinet["A-3"]
print(cabinet)