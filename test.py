

def solution(s):
    return ''.join(sorted(list(s), reverse=True))


num = input()
print(solution(num))