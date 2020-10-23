# 4-6  씨름선수 그리디
# N 명의 씨름선수가 있을 때
# 키와 몸무게 가 주어질때 지원자 일대일 비교했을 때 키 몸무게 둘 중 하나라도 높아야 뽑힌다.


import sys
sys.stdin = open("input.txt", "rt")

n = int(input())
body = []
for i in range(n):
    h, w = map(int, input().split())
    body.append((h, w))
body.sort(reverse=True)
print(body)
largest=0
cnt=0
for x,y in body: #X=height y= weight
    if y>largest:
        largest = y
        cnt +=1
        print((x,y))
print(cnt)

"""
5
172 67
183 65
180 70
170 72
181 60
"""