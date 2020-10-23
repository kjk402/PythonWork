
from random import *
# lst = [1,2,3,4,5]
# print(lst)
# shuffle(lst)
# print(lst)
lst = range(1,21) #1부터 20까지 숫자 생성
print(type(lst))
lst = list(lst)
print(type(lst))
print(lst)

shuffle(lst)
print(lst)

winners = sample(lst, 4) #4명 뽑고

print("==당첨자==")
print("치킨 당첨자 : {0}".format(winners[0]))
print("커피 당첨자 : {0}".format(winners[1:]))
print("==축하합니다==")
