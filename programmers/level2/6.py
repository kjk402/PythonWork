#6번 더맵게


def solution(scoville, K):
    answer = 0
    scoville.sort()
    now = 0
    if scoville[0] >= K:
        return answer
    for _ in range(len(scoville)):
        now += scoville[0] + (scoville[1]*2)
        answer+=1
        del scoville[0:2]
        scoville.append(now)
        scoville.sort()
        if scoville[0] >= K:
            break
        else:
            if len(scoville)>2:
                now =0
            else:
                return -1

    return answer


s = [1, 2, 3, 9, 10, 12]
k = 7
print(solution(s,k))
