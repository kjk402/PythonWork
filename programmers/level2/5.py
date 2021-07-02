#5 문자열 압축

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