# 5 모험가 길드

people = list(map(int, input().split()))

people.sort()
result = 0
cnt = 0
for i in people:
    cnt +=1
    if cnt >=i:
        result +=1
        cnt =0
print(result)

"""
2 3 1 2 2 
"""