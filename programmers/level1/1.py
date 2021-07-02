# 크레인 인형 뽑기

def solution(board, moves):
    answer =0
    bucket = []
    for move in moves:
        for i in range(len(board)):
            if board[i][move-1]: # 존재할때
                bucket.append(board[i][move-1]) # bucket에 뽑기
                board[i][move-1] = 0 # 0으로 바꾸기

                if len(bucket) > 1 and bucket[-1] ==bucket[-2]:
                    bucket.pop()
                    bucket.pop()
                    # 뒤에 중복 두개면 빼기
                    # del bucket[-2:]
                    answer +=2
                break
    return answer




# 지금 보드의 len은 5이다
board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
# print(len(board))
moves = [1,5,3,5,1,2,1,4]
#
print(solution(board, moves))