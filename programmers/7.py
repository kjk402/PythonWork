def solution(numbers, hand):
    answer = ''
    for i in numbers:
        if i == 1 or i==4 or i==7:
            answer += 'L'
        elif i == 3 or i==6 or i ==9:
            answer +='R'
    return answer


num = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
print(solution(num))