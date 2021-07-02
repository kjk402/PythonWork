# 27번 카펫


def solution(brown, red):
    for i in range(1,red//2+2) :
        for j in reversed(range(red//i+1)) :
            if i*j == red :
                if 2*(i+j)+4 == brown :
                    return [max(i,j)+2, min(i,j)+2]
                break
    return

# def solution(brown, yellow):
#     answer = []
#     print(b, y)
#     sum = b+y
#     for i in range(1, brown//2 +1):
#         for j in range(1, brown//2 +1):
#             if i*j ==sum:
#                 answer.append((i,j))
#
#     if len(answer) >2:
#         answer = list(set(answer))
#     answer.sort(reverse=True)
#     return answer


b = 24
y = 24
print(solution(b, y))