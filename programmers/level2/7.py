#7번 큰 수 만들기

def solution(number, k):
    s = []
    cnt = 0
    for i in number:
        if cnt == k:
            s.append(i)
        else:
            if not s:
                s.append(i)
                print(s)
            else:
                while s:
                    if cnt == k or i <= s[-1]:
                        break
                    if i > s[-1]:
                        s.pop()
                        cnt += 1
                s.append(i)

    while cnt !=k:
        s.pop()
        cnt += 1
    return ''.join(s)


num = "1924"
k = 2
print(solution(num, k))