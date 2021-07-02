# 29번 튜플

def solution(s):
    answer = []
    s = s[2:-2]
    s = s.split('},{')

    s.sort(key= len)
    for x in s:
        l = x.split(',')
        for y in l:
            if int(y) not in answer:
                if y.isdecimal:
                    answer.append(int(y))

    return answer

s = "{{2},{2,1},{2,1,3},{2,1,3,4}}"
print(solution(s))