#while

customer = "Thor"
index = 5
while index >= 1 :
    print("{0}, 커피가 준비되었습니다. {1}번 남았어요,".format(customer, index))
    index -= 1
    if index == 0:
        print("커피 버림")

#
# index = 1
# while True:
#     print("{0} 커피나왔다. 호출{1}회".format(customer, index))
#     index += 1
#     if index == 100:
#         print("커피 버림")


customer = "아이언맨"
person = "Unknown"

while person != customer :
    print("{0}님 커피 나왔습니다.".format(customer))
    person = input("이름밝혀")
    if person == "아이언맨" :
        print("맛있게 드세요.")
