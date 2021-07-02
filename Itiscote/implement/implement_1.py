# 1 상하좌우

#

a =1
b =1

n = int(input())
order = list(input().split())

print(order)

for x in order:
    if x == 'R':
        if b!=5:
            b +=1
    if x == 'L':
        if b!=1:
            b -=1
    if x == 'U':
        if a != 1:
            a -=1
    if x == 'D':
        if a!= 5:
           a +=1
print(a, b)



"""
5
R R R U D D
"""