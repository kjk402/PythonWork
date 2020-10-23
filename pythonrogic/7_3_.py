#변수

gun =10

def checkpoint(soldiers): #경계근무
    global gun
    gun = gun -soldiers # 경계근무하는 수 만큼 총 갯수 빼기
    print("[함수 내] 남은 총 : {0}".format(gun))



print("전체총 :{0}".format(gun))
checkpoint(2)
print("남은총:{0}".format(gun))