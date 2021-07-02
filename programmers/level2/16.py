# 16번 H-index

def solution(citations):
    citations.sort(reverse=True)
    answer = max(map(min, enumerate(citations, start=1)))
    return answer


c = [3,0,6,1,5]
print(solution(c))


"""
def solution(citations):
    answer = 0
    citations = list(citations)
    citations.sort()

    for i in range(len(citations)):
        cnt = 0
        if citations[i] <= max(citations[i+1:]):
            cnt += len(citations)-i
            if cnt == citations[i]:
                answer += cnt
                break
        
    return answer
"""