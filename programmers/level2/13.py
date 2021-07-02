# 13번 스킬트리

# def solution(skill, skill_trees):
#     answer = []
#     for x in skill_trees:
#         for j in skill:
#             if j not in x:
#                 skill_trees.remove(x)
#
#     return answer

def solution(skill, skill_trees):

    skill = list(skill)
    flag = []
    for i in skill_trees:
        # 가능한 스킬인지 검증
        post_skill_trees = []
        for j in list(i):
            if j in skill:
                post_skill_trees.append(j)

        for idx, j in enumerate(post_skill_trees):
            if j != skill[idx]:
                flag.append(-1)
                break

    return len(skill_trees) + sum(flag)
s = "CBD"
skil = ["BACDE", "CBADF", "AECB", "BDA"]
print(solution(s, skil))

# for x in skil:
#     answer =[]
#     for j in x:
#         print(j)
#         print(s)
#         if j in s:
#             answer.append(j)
#     print(answer)
#     answer = []



