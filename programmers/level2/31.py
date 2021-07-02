# 31번 이진변환 반복하기

def solution(s):
    answer = []



    print(len(s))
    bnt = 0
    cnt = 0
    while len(s)>1:
        y = []
        for x in s:
            if x == '0':
                cnt+=1
            else:
                y.append(x)

        if len(y)>=1:
            s = ''.join(y)
            s = bin(len(s))[2:]
            bnt +=1
    answer.append(bnt)
    answer.append(cnt)
    return answer


"""
def solution(s):
    count=0
    change=0

    while s!='1':
        l=len(s)
        count+=l-s.count('1')
        s=str(bin(s.count('1'))[2:])
        change+=1
    return [change,count]
"""

s = "110010101001"
k = "1111111"
print(solution(s))
print(solution(k))

