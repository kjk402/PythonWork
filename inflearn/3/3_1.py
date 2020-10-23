# 3-1 회문 문자열 검사

# 앞에나 뒤에서 읽을 때 같은 문자 판별
# level  abba

import sys
sys.stdin = open("../4/input.txt", "rt", encoding="utf8")

n = int(input())
for i in range(n):
    string = input()
    string = string.upper()
    size = len(string)

    for j in range(size//2):
        if string[j] != string[-1-j] :
            print("#%d NO" %(i+1), string)
            break
    else:
        print("#%d YES" %(i+1), string)

# 5
# level
# moon
# abcba
# soon
# gooG