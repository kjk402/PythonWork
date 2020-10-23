# 3-2 숫자만 추출

# 문자와 숫자가 섞여있는 문자열이 주어지면 그 중 숫자만 추출 1.
# 2. 추출된 숫자의 약수 개수 출력

import sys
sys.stdin = open("../4/input.txt", "rt")

string = input()
res = 0
for x in string:
    if x.isdecimal():
        res = res * 10 +int(x)
print(res)
cnt = 0
for i in range(1, res+1):
    if res%i ==0:
        cnt +=1
        print(i, end=' ')
print()
print(cnt)


# g0en2Ts8eSoft
