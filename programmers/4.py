def solution(answers):
    acnt = 0
    bcnt = 0
    ccnt = 0

    answer = []
    a = []
    while len(a) < len(answers):
        for i in range(1, 6):
            a.append(i)
    b = []
    bb = [2, 1, 2, 3, 2, 4, 2, 5]
    while len(b) < len(answers):
        for j in bb:
            b.append(j)
    c = []
    cc = [3,3,1,1,2,2,4,4,5,5]
    while len(c) < len(answers):
        for k in cc:
            c.append(k)
    for s in range(len(answers)):
        if a[s] == answers[s]:
            acnt+=1
    for d in range(len(answers)):
        if b[d] == answers[d]:
            bcnt+=1
    for f in range(len(answers)):
        if c[f] == answers[f]:
            ccnt+=1

    if acnt > bcnt and acnt >ccnt:
        answer.append(1)
    elif acnt == bcnt and acnt >ccnt:
        answer.append(1)
        answer.append(2)
    elif acnt == ccnt and acnt >bcnt:
        answer.append(1)
        answer.append(3)

    elif bcnt > acnt and bcnt > ccnt:
        answer.append(2)
    elif bcnt == acnt and bcnt > ccnt:
        answer.append(1)
        answer.append(2)
    elif bcnt == ccnt and bcnt > acnt:
        answer.append(2)
        answer.append(3)

    elif ccnt > acnt and ccnt > bcnt:
        answer.append(3)
    elif ccnt == acnt and ccnt > bcnt:
        answer.append(1)
        answer.append(3)
    elif bcnt == ccnt and ccnt > acnt:
        answer.append(2)
        answer.append(3)


    elif acnt == bcnt and acnt == ccnt:
        answer.append(1)
        answer.append(2)
        answer.append(3)


    return answer





