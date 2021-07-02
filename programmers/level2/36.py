# 36번 영어 끝말잇기

def solution(n, words):
    # 처음으로 말한 단어 저장
    dataset = set([words[0]])

    # 이전 단어 기억
    prev_words = words[0]

    for i in range(1, len(words)):
        # 이전 단어의 마지막 글자와 제시단어의 첫글자가 다르거나, 이미 있는 단어일 경우
        if (prev_words[-1] != words[i][0]) or words[i] in dataset:
            # 사람, 차례
            return [(i % n) + 1, (i // n) + 1]
        # 등장한 단어 저장
        dataset.add(words[i])
        # 제시단어 기억
        prev_words = words[i]
    return [0, 0]


"""
def solution(n, words):
    answer = [0, 0]
    count = 1 # range가 1부터 시작하므로, 1으로 설정 
    for idx in range(1, len(words)): # 1부터 시작하는 이유는 첫번째 사람의 첫 단어는 절대 틀릴 일이 없음 
        word = words[idx] # words[idx] : 언급된 단어 
        count %= n 
        if (word in words[0:idx]) or (words[idx-1][-1] != word[0]): 
            answer = [count +1, 1 + idx//n]
            return answer 
        count +=1 
    return answer
"""