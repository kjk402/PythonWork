# 게임 개발

n, m = map(int, input().split())

x, y, direction = map(int, input().split())

# 지나간 곳은 1로 표시, 처음 시작부분을 제외하고는 0으로 초기화
d = [[0] * m for _ in range(n)]
d[x][y] = 1


# 전체 맵 받기
array = []
for i in range(n):
    array.append(list(map(int, input().split())))

print(d)
print(array)


dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 0 북쪽 // 1 동쪽// 2 남쪽 // 3 서쪽

def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

cnt = 1
# 네 방향 확인 turn time
turn_time = 0

while True:
    # 1 단꼐 왼쪽으로 회전
    turn_left()
    nx = x+dx[direction]
    ny = y+dy[direction]

    # 회전 후 정면에 가보지 않은 칸 존재하면 한칸 이동 (육지일때 -> array)
    if d[nx][ny] ==0 and array[nx][ny] ==0:
        d[nx][ny] = 1
        x = nx
        y = ny
        cnt +=1
        turn_time = 0
        continue
    # 회전 후 정면에 가보지 않은 칸이 없고, 바다일때
    else:
        turn_time +=1

    # 네방향 모두 확인 했을 때 ->한칸 뒤로가고1단계로 돌아간다.
    if turn_time ==4:
        nx = x-dx[direction]
        ny = y-dy[direction]

        #뒤로 갈 수 있는 경우
        if array[nx][ny] ==0:
            x=nx
            y=ny

        #뒤가 바다인 경우
        else:
            break

        turn_time = 0

print(cnt)













"""
4 4 
1 1 0
1 1 1 1 
1 0 0 1
1 1 0 1
1 1 1 1
"""
