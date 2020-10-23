# 2-4 대표값

import sys
sys.stdin = open("input.txt", "rt", encoding="utf8")

n = int(input())
a = list(map(int, input().split()))

aver = round(sum(a)/n)
min=214700000
for id, x in enumerate(a):
    tmp = abs(x-aver)
    if tmp<min:
        min=tmp
        score = x
        answer = id +1
    elif tmp==min:
        if x > score:
            score = x
            answer = id +1
print(aver, answer)


# 10
# 45 73 66 87 92 67 75 79 75 80

r = 4.523
print(round(r))
print(abs(r))