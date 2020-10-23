# 4-5 회의실 배정 그리디 문제

# 회의실을 사용해야 하는 횟수가 N 일때
# 무작위로 시작 시간, 끝나는 시간 주어질 때  최대 수의 회의를 찾아라

import sys
sys.stdin = open("input.txt", "rt")

n = int(input())
meeting = []
for i in range(n):
    sp, ep = map(int,input().split())
    meeting.append((sp, ep))
meeting.sort(key=lambda x : (x[1], x[0]))  # ep 기준으로 정렬하는 법
et = 0 # endtime
cnt = 0
for sp, ep in meeting:
    if sp>=et:
        et = ep
        cnt+=1
        print((sp, ep))
print(cnt)


"""
5
1 4
2 3
3 5
4 6
5 7
"""