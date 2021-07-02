# jadenCase

def solution(s):
    answer = []

    s= list(map(str, s.split(' ')))

    for i in range(len(s)):
        if s[i][0].isalpha():
            s[i] = s[i][0].upper() +s[i][1:].lower()

    return ' '.join(s)


s = "3people unFollowed me"
print(solution(s))

"""
def solution(s):
    s = s.lower()
    L=s.split(" ")
    answer = ""
    for i in L:
        i= i.capitalize()
        answer+= i+" "
    return answer[:-1]
"""