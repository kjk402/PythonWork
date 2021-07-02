# 32번 피보나치 수

def solution(n):
    Table = [0 for c in range(n+1)]
    Table[1] = 1
    for i in range(2, n+1):
        Table[i] = (Table[i-1] + Table[i-2]) % 1234567

    return Table[i]


"""
def solution(num):
    a,b = 0,1
    for i in range(num):
        a,b = b,a+b
    return a
"""

"""
def solution(n):
    a = 0
    s = 1
    for i in range(n-1):
        r=a+s
        a=s
        s=r
    return s%1234567
"""