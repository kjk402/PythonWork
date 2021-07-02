# 7 문자열 압축
# answer = []
#     a = []
#     while len(a) < len(answers):
#         for i in range(1, 6):
#             a.append(i)
#     b = []
#     bb = [2, 1, 2, 3, 2, 4, 2, 5]
#     while len(b) < len(answers):
#         for j in bb:
#             b.append(j)

def solution(s):
    answer = len(s)
    for step in range(1, len(s) // 2 + 1):
        compressed = ""
        prev = s[0:step]
        cnt = 1
        for j in range(step, len(s), step):
            if prev == s[j:j + step]:
                cnt += 1
            else:
                if cnt >= 2:
                    compressed += str(cnt) + prev
                else:
                    compressed += prev
                prev = s[j:j + step]
                cnt = 1
        compressed += str(cnt) + prev if cnt >= 2 else prev

        answer = min(answer, len(compressed))

    return answer