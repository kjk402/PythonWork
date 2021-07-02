def solution(s):
    answer = ""
    s = list(map(int, s.split(' ')))
    s.sort()
    print(s)
    answer += str(s[0]) +" "+ str(s[-1])

    return answer


s = "-1 -2 -3 -4"
print(solution(s))

"""

def solution(s):
    answer = []
    s = list(map(int, s.split(' ')))
    s.sort()
    print(s)
    answer.append(s[0])
    answer.append(s[-1])
    return answer
"""