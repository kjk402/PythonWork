def solution(numbers):
    answer = []
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if i == j:
                pass
            else:
                answer.append(numbers[i] + numbers[j])

    answer = set(answer)
    return answer

number = [5,0,2,7]

print(solution(number))