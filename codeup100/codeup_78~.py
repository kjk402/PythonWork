# 78 짝수 합 구하기

# count = int(input())
# num = 0
# for i in range(0, count+1):
#      if i%2 ==0:
#          num+= i
# print(num)

# 79 원하는 문자가 나올 때까지 출력하기
# var = input()
# word = input().split(' ')
# for w in word:
#     print(w)
#     if w == var:break

# 80
# end_point = int(input())
#
# total = 0
# for i in range(1, end_point+1):
#   total += i
#   if total >= end_point:
#     print( i )
#     break

# 81 1부터 N 까지 1부터 M까지 적힌 두 주사위 던져서 나오는 경우의 수 출력
# n, m = map(int, input().split(' '))
# for n in range(1, n+1):
#     for m in range(1, m+1):
#         print(n, m)

# 82 16진수 구구단
# hexa = '0x' +input()
# for i in range(1, 16):
#     print(hexa[2:],"*" ,hex(i)[2:].upper(),"=", \
#           hex(int(hexa, 16) * i)[2:].upper(),sep='')

# char = input()
# for i in range(1, 16):
#     print("{0}*{1}={2}".format(char, hex(i)[2:].upper(), hex(int(char, 16) * i)[2:].upper()))


# 83  369 게임
#
# #3의 배수만 X 표시
# num = int(input())
# for i in range(1, num+1):
#     if i%3 == 0:
#         print("X", end=' ')
#     else:
#         print(i, end=' ')
#
# # 3 6 9 들어가 있으면 X 표시
# num = int(input())
# for i in range(1, num+1):
#     if '3' in str(i) or '6' in str(i) or '9' in str(i):
#         print("X", end=' ')
#     else:
#         print(i, end=' ')


# 84 rgb 경우의 수 출력
# r, g, b = map(int, input().split(' '))
# cnt = 0
# for i in range(r):
#     for j in range(g):
#         for k in range(b):
#             print(i, j, k)
#             cnt +=1
#
# print(cnt)
#

# 85 소리 파일 저장용량 계산하기
# h, b, c, s = map(int, input().split(' '))
# result = h*b*c*s
# resultMB = result / (8*1024 **2)
# print(round(resultMB, 1), 'MB')

# 86 그림 파일 저장용량 계산하기
# w, h, b = map(int, input().split())
# result = (w*h*b) / (8 * 1024**2)
# print( round(result, 2))
# print("MB")

# 87
# end_point = int(input())
# total = 0
# i = 1
# while total < end_point:
#     total += i
#     i += 1
# print(total)

#88 3의 배수는 통과
# num = int(input())
# for i in range(1, num+1):
#   if i%3 !=0:
#     print(i, end=' ')
#   else:
#     continue


#89 등차
# a, d, n = map(int, input().split(' '))
#
# i =a
# count=0
# arith = []
# while count < n:
#   arith.append(i)
#   i += d
#   count += 1
# print(arith)


#90 등비
# a,r,n = map(int, input().split(' '))
# i = a
# count = 0
# arith=[]
# while count < n:
#     arith.append(i)
#     i *= r
#     count+=1
# print(arith[-1])

# #91 등차 등비 응용
# a,m,d,n = map(int, input().split(' '))
# i = a
# count = 0
# arith=[]
# while count < n:
#     arith.append(i)
#     i *= m
#     i += d
#     count+=1
# print(arith[-1])

#92 세수의 최소 공배수 구하기
# a, b, c = map(int, input().split(' '))
# day = 1
# while day%a !=0 or day%b !=0  or day%c !=0:
#   day +=1
#
# print(day)























