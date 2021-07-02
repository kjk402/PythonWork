# 1번

def solution(grades, weights, threshold):
    answer = 0

    for i in range(len(weights)):
        if grades[i] == "A+":
            answer += weights[i] * 10
        if grades[i] == "A0":
            answer += weights[i] * 9
        if grades[i] == "B+":
            answer += weights[i] * 8
        if grades[i] == "B0":
            answer += weights[i] * 7
        if grades[i] == "C+":
            answer += weights[i] * 6
        if grades[i] == "C0":
            answer += weights[i] * 5
        if grades[i] == "D+":
            answer += weights[i] * 4
        if grades[i] == "D0":
            answer += weights[i] * 3
        if grades[i] == "F":
            answer += weights[i] * 0


    return answer-threshold


g = ["A+","D+","F","C0"]
w = [2,5,10,3]
t = 50
print(solution(g, w, t))