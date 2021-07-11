# 로또의 최고 순위와 최저 순위
# https://programmers.co.kr/learn/courses/30/lessons/77484

def solution(lottos, win_nums):
    answer = [0, 0]
    count = 0
    rank = [6, 6, 5, 4, 3, 2, 1]
    for i in lottos:
        if i in win_nums:
            count +=1

    answer[0] = rank[count + lottos.count(0)]
    answer[1] = rank[count]
    return answer
