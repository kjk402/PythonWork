def solution(n, board):
    answer = 0
    stack = []
    for i in board:
        for x in i:
            stack.append((x,i.index(x)+1))
    for i in range(1, n*n):
        if stack[0][i]



    return stack



n = 3
b =[[3, 5, 6], [9, 2, 7], [4, 1, 8]]
print(solution(n, b))