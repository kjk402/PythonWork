def solution(n):
    cnt =0


    for x in range(1, n+1):
        # if len(x) < 3 :
            if '3'in str(x) or '6' in str(x) or '9' in str(x):
                cnt +=1

    return cnt


num = 33

print(solution(num))

