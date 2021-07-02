# 6번

def solution(logs):
    answer = []
    logs = list(logs)
    logs.sort(key=lambda x : int(x[0]))
    second = []
    for i in range(len(logs)):

        second.append(logs[i][0:4])

    print(logs)
    second = set(second)
    print(second)
    print(len(second))

    return answer



lg = ["1901 1 100", "1901 2 100", "1901 4 100", "1901 7 100", "1901 8 100", "1902 2 100", "1902 1 100", "1902 7 100", "1902 4 100", "1902 8 100", "1903 8 100", "1903 7 100", "1903 4 100", "1903 2 100", "1903 1 100", "2001 1 100", "2001 2 100", "2001 4 100", "2001 7 95", "2001 9 100", "2002 1 95", "2002 2 100", "2002 4 100", "2002 7 100", "2002 9 100"]

print(solution(lg))