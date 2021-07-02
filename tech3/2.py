# 2번


def solution(s, op):
    answer = []

    for i in range(len(s)-1):
        lt = s[:i+1]
        rt = s[i+1:]
        if op == "+":
            answer.append(int(lt)+int(rt))
        if op == "-":
            answer.append(int(lt) - int(rt))
        if op == "*":
            answer.append(int(lt) * int(rt))
    return answer



s= "1234"
op ="+"

print(solution(s,op))