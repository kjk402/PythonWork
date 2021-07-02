# 15번 가장 큰 수

def solution(numbers):
    answer = ''
    numbers = list(map(str, numbers))
    numbers.sort(key= lambda x: x *3, reverse=True)
    answer = str(int(''.join(numbers)))

    return answer


num= [6, 10, 2]
print(solution(num))