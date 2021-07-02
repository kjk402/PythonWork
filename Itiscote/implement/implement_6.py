# 문자열 재정렬

# 알파벳 먼저, 숫자는 뒤에

n = input()
alpha = []
num =0

for i in n:
    if i.isalpha():
        alpha.append(i)
    else:
        num += int(i)

alpha.sort()


if num !=0:
    alpha.append(str(num))

print(''.join(alpha))