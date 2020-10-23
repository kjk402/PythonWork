def solution(array, commands):
    answer = []
    return answer
def solution(array, commands):
    answer = [0, 0, 0]
    for i in range(3) :
        arr = array[commands[i][0]-1:commands[i][1]]
        leng = commands[i][1]-commands[i][0]+1
        for j in range(leng) :
            for k in range(j, leng) :
                if arr[j]>arr[k] :
                    t = arr[j]
                    arr[j] = arr[k]
                    arr[k] = t
        answer[i] = arr[commands[i][2]-1]
    return answer