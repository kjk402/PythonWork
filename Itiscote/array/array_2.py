# 2 성적이 낮은 순서로 학생 출력하기

n= int(input())

a = []
for i in range(n):
    data = input().split()
    a.append((data[0], int(data[1])))

print(a)
"""
2
홍길동 99
이순신 77
"""

a.sort(key=lambda s: s[1])
print(a)
for student in a:
    print(student[0], end=' ')