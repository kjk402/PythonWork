#10 같은 숫자는 싫어
"""
"""

def solution(arr):
    answer = []
    if len(arr) ==1:
        return arr
    answer.append(arr[0])


    for i in range(1, len(arr)):
        if arr[i] != arr[i-1]:
            answer.append(arr[i])


    return answer


arr =[4,4,4,3,3]
print(solution(arr))