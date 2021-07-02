#23 최솟값 만들기


def solution(A,B):
    A, B = sorted(A),sorted(B, reverse=True)
    answer = 0
    for i in range(len(A)):
        answer += A[i]*B[i]
    return answer


a = [1, 4, 2]
b = [5,4,4]
print(solution(a, b))