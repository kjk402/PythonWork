# 5-8  단어 찾기
import sys
sys.stdin = open("input.txt", "rt", encoding='utf8')


all = []
write = []


n = int(input())

for _ in range(n):
    word = input()
    all.append(word)
print(all)

for _ in range(n-1):
    word2 = input()
    write.append(word2)
print(write)

for x in all:
    if x not in write:
        print(x)
    else:
        pass



"""
12
student
kind
teacher
big
good
sky
blue
dkfkjgk
mouse
back
tom
dkfjkqhgk
sky
good
mouse
big
blue
dkfkjgk
tom
dkfjkqhgk
student
teacher
back

"""