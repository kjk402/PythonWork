# 65 세 정수 입력받고 짝수만 출력

# a, b , c= map(int, input().split(' '))
# 방법 1 조건문 사용
# if not a%2: print(a)
# if not b%2: print(b)
# if not c%2: print(c)

#방법 2 filter 함수 사용
# print(*filter(lambda num: num%2 == 0, [a, b, c]))


# 66 even짝수 odd 홀수 출력
# a, b , c= map(int, input().split(' '))
# print(a%2 and 'odd' or 'even')
# print(b%2 and 'odd' or 'even')
# print(c%2 and 'odd' or 'even')


#67 숫자 음 양 홀 짝 판별
# num = int(input())
# if num <= 0:
#     print('minus')
# else:
#     print('plus')
# if abs(num)%2 == 0:
#     print('even')
# else:
#     print('odd')

#68 성적 산출
# num = int(input())
# if num >= 90:
#     print('A')
# elif num >= 70:
#     print('B')
# elif num >= 40:
#     print('C')
# else:
#     print('D')

#69 문자 입력 =>
# grade = input()
# if grade == 'A':
#     print("best!!!")
# elif grade == 'B':
#     print("good!!")
# elif grade == 'C':
#     print("run!")
# elif grade == 'D':
#     print("slowly~")
# else:
#     print('what?')

#70
# month = int(input())
# if month==12 or month==1 or month==2:
#     print("winter")
# elif month==3 or month==4 or month==5:
#     print("spring")
# elif month==6 or month==7 or month==8:
#     print("summer")
# else:
#     print('fall')

#71
# def goto(inteager, i):
#     if inteager[i] == 0:
#         return
#     else:
#         print(inteager[i])
#         i += 1
#         goto(inteager, i)
#
# inteager = list(map(int, input().split(' ')))
# goto(inteager, i = 0)

#72
# num1 = int(input())
# num2 = list(map(int, input().split(' ')))
#
# def goto(num2, num1, i):
#     if i == num1:return
#     print(num2[i])
#     i += 1
#     goto(num2, num1, i)
#
# goto(num2, num1, 0)

#73
# num = list(map(int, input().split(' ')))
#
# for var in num:
#     if var == 0:break
#     else:
#         print(var)

#74 카운트다운
# num = int(input())
# while num >= 1:
#     print(num)
#     num -= 1
#     if num == 0:
#         break

# #75 카운트다운
# num = int(input())
# while num >= 0:
#     num -=1
#     print(num)
#     if num <= 0:
#         break

#76
# order = ord(input())
# print(chr(order+1))
# var = ord(input())
# while int(var) >= 65:
#     print(chr(var))
#     var -= 1
#     if int(var) < 65:
#         break

# var = ord(input())
# for i in range(65, var+1, +1):
#     print(chr(i), end=' ')


# converter = ord(input())
#
# for i in range(97, converter+1):
#   print( chr(i), end=' ' )


#77 숫자 입력받고 그 숫자까지 출력받기
# count = int(input())
# for i in range(0, count+1):
#     print(i)