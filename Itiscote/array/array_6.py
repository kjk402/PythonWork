# 6 실패율


def solution(n, stages):
    answer = []
    length = len(stages)


    for i in range(1, n+1):
        cnt = stages.count(i)

        if length==0:
            fail =0
        else:
            fail = cnt /length

        answer.append((i,fail))
        length -=cnt

    answer.sort(key= lambda x: x[1], reverse=True)

    answer = [i[0] for i in answer]
    return answer

num = 5
s = [2, 1, 2, 6, 2, 4, 3, 3]
print(solution(num, s))


"""
def solution(n, stages):
    answer = []
    stage = []
    cnt = 0
    result=[]
    m = len(stages)
    for x in stages:
        if x < n:
            stage.append(x)
    print(stage)
    stage.sort()
    for i in range(1, n+1):
        for x in stage:
            if x == i:
                cnt += 1
        answer.append((i, (cnt/m)))
        m -= cnt
        cnt = 0
    answer.sort(key= lambda s: -s[1])
    for i in answer:
        result.append(i[0])
    return result
"""