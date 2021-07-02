# 5-7 교육과정 설계
# import sys
# sys.stdin = open("input.txt", "rt", encoding='utf8')


sub = input()
n = int(input())
answer = []

sub = list(sub)

for _ in range(n):
    plan = input()
    plan = list(plan)
    for x in range(len(plan)):
        for i in range(len(sub)):
            if plan[x] == sub[i]:
                answer.append(plan[x])
            else:
                pass

    print(sub)
    print(answer)

    if sub != answer:
        print("NO")
    else:
        print("YES")
    answer = []



"""
AKDEF
5
AYKGDHEJ
AQKWDERTFYP
CTFKSBDEA
ASKGHDEF
WOPASFKGHDEF

 = > n y n y n
"""