# 4 국영수

n = int(input())
a = []
for _ in range(n):
    a.append(input().split())

a.sort(key= lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for i in a:
    print(i[0])

"""
12
Junkyu 50 60 100
Sangkeun 80 60 50
Sunyoung 80 70 100
Soong 50 60 90
Haebin 50 60 100
Kangsoo 60 80 100
Donghyuk 80 60 100
Sei 70 70 70
Wonseob 70 70 90
Sanghyun 70 70 80
nsj 80 80 80
Taewhan 50 60 90
"""