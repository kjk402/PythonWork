# 5-9 아나그램
# 문자열에서 문자 순서가 달라도 구성과 갯수가 같으면
# 같은 문자로 판별해주는 것

import sys
sys.stdin = open("input.txt", "rt", encoding='utf8')

word1 = input()
word2 = input()

wordlist1 = []
wordlist2 = []

for x in word1:
    wordlist1.append(x)
for x in word2:
    wordlist2.append(x)

wordlist1.sort()
wordlist2.sort()
print(wordlist1)
print(wordlist2)
if wordlist1==wordlist2:
    print("YES")
else:
    print("NO")
