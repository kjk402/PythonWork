
def solution(pobi, crong):

    pobi = calmax(pobi)
    crong = calmax(crong)

    if pobi>crong:
        return 1
    elif crong>pobi:
        return 2
    elif pobi == crong:
        return 0



def calmax(num):
    num1 = str(num[0])
    num2 = str(num[1])
    lsum = 0
    lmul = 1
    rsum = 0
    rmul = 1

    for i in num1:
        lsum += int(i)
        lmul *= int(i)
    for j in num2:
        rsum += int(j)
        rmul *= int(j)

    return max(max(lsum, lmul), max(rsum, rmul))



p = [97, 98]
c = [211,212]

print(solution(p, c))