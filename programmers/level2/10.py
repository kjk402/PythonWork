#10번 구명보트

def solution(people, limit):
    answer = 0
    people.sort()

    while people:
        if len(people) ==1:
            answer+=1
            break
        if people[0] +people[-1] >limit:
            people.pop()
            answer +=1
        else:
            people.pop()
            people.pop(0)
            answer +=1
    return answer


print(solution([70, 50, 80, 50], 100))