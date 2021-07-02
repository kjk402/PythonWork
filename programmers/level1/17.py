# 17번 서울에서 김서방 찾기

def solution(seoul):
    cnt = 0
    for x in seoul:
        if x=="Kim":
            break
        else:
            cnt+=1

    return "김서방은 " + str(cnt) + "에 있다"

s = ["Jane", "Kim"]
print(solution(s))