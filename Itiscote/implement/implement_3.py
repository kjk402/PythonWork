# 3 왕실의 나이트

n=input()

row = int(n[1])
column = int(ord(n[0])-int(ord('a'))) +1

steps = [(2,-1), (2,1), (1,2), (-1,2), (-2,-1), (-2,1), (1,-2), (-1,-2)]
cnt=0
for i in steps:
    next_row = row + i[0]
    next_column = column + i[1]

    if next_row >=1 and next_row <=8 and next_column >=1 and next_column<=8:
            cnt+=1

print(cnt)



"""
a1 
=> 2
"""