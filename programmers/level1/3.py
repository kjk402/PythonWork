# 완주하지 못한 선수


def solution(party, complet):
    party.sort()
    complet.sort()
    answer = []
    for person in party:
        if person not in complet:
            answer.append(person)

        else:
            complet.pop(0)
    return answer


p =["mislav", "stanko", "vinko","mislav", "ana","marina","vinko"]
c = ["stanko", "ana", "mislav", "marina","vinko"]

print(solution(p, c))

"""
def solution(participant, completion):

    participant.sort()
    completion.sort()

    for i in range(len(completion)):
        if participant[i] != completion[i]:
            return participant[i]
    return participant[i+1]
"""