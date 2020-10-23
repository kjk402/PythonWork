


# #13
# var = list(map(int, input()))
# print(var[0], var[1], end="")
#
#
# var = list(map(int, input().split()))
# print(var[0], var[1])

# #14
# var = input().split()
# print(var[1], var[0])

#15
# var = float(input())
# print(round(var,2))
#
# var = round(float(input()), 2)
# print(var)

#18
# y,m,d = input().split('.')
# print("{0}.".format(y).zfill(5),"{0}.".format(m).zfill(3),"{0}".format(d).zfill(2),sep='')
#
# y,m,d = input().split('.')
# if len(y) == 2:
#     y = '00'+ y
# if len(m) == 1:
#     m = '0' + m
# if len(d) == 1:
#     d = '0' + d
# print('{0}.{1}.{2}'.format(y, m, d))

#19
# birth, num = input().split('-')
# print("{0}{1}".format(birth, num).zfill(13))

# #20,21
# var = input()
# print(var)

# #22
# n, s = input().split('.')
# print("{0}\n{1}".format(n, s))

#24
# string = input()
# for i in range(len(string)):
#     print("'{}'".format(string[i]))


#25
# integer = input()
# count = len(integer)-1
# for i in range(len(integer)):
#     print([int(integer[i]+ '0'*count)])
#     count -= 1

#26
# h, m, s = input().split(":")
# 
# print(str(m))

#27
# y, m, d = input().split(".")
# if len(y) == 2:
#     y = '00'+y
# if len(m) == 1:
#     m = '0' + m
# if len(d) == 1:
#     d = '0' + d
#
# print("{0}-{1}-{2}".format(d, m, y))






















