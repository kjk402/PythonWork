# 재귀 용법 reversive call
# 함수 안에서 동일한 함수를 호출하는 형태

# 팩토리얼
# def factorial(num):
#     if num > 1:
#         return num * factorial(num - 1)
#     else:
#         return num
#
# var = int(input())
# print(factorial(var))


# 리스트 합구하기

# def sum_list(data):
#     if len(data) <=1:
#         return data[0]
#     else:
#         return data[0] + sum_list(data[1:])
#
# var = list(map(int, input().split()))
# print(sum_list(var))

# 회문 구하기
# def palindrome(string):
#     if len(string) <= 1:
#         return True
#
#     if string[0] == string[-1]:
#         return palindrome(string[1:-1])
#     else:
#         return False
#
# var = input()
# print(palindrome(var))


def func(data):
    if data == 1:
        return 1
    elif data == 2:
        return 2
    elif data == 3:
        return 4

    return func(data - 1) + func(data - 2) + func(data - 3)

print(func(6))







