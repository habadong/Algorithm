import sys
sys.stdin = open("예제.txt", "r")
import math

r, c, t = map(int, input().split())
room = [list(map(int, input().split())) for i in range(r)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
answer = 0

def diff(x, y): 
    count = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < r and 0 <= ny < c:
            if room[nx][ny] >= 0:
                diff_room[nx][ny] += math.floor(room[x][y]/5)
                count += 1
    remain_room[x][y] = room[x][y] - (math.floor(room[x][y]/5) * count)

def air_clean(top, bottom):
    for i in range(top, 0, -1):
        room[i][0] = room[i-1][0]

    for i in range(c-1):
        room[0][i] = room[0][i+1]

    for i in range(0, top):
        room[i][c-1] = room[i+1][c-1]

    for i in range(c-1, 1, -1):
        room[top][i] = room[top][i-1]

    room[top][0] = -1
    room[top][1] = 0

    for i in range(bottom, r-1):
        room[i][0] = room[i+1][0]

    for i in range(c-1):
        room[r-1][i] = room[r-1][i+1]

    for i in range(r-1, bottom, -1):
        room[i][c-1] = room[i-1][c-1]

    for i in range(c-1, 1, -1):
        room[bottom][i] = room[bottom][i-1]

    room[bottom][0] = -1
    room[bottom][1] = 0

while t > 0:
    diff_room = [[0]*c for i in range(r)]
    remain_room = room.copy()
    for i in range(r):
        for j in range(c):
            if room[i][j] > 0:
                diff(i, j)

    for i in range(r):
        for j in range(c):
            room[i][j] = diff_room[i][j] + remain_room[i][j]
            
    for i in range(r):
        if room[i][0] == -1:
            air_clean(i, i+1)
            break
    t -= 1

for i in range(r):
    for j in range(c):
        if room[i][j] > 0:
            answer += room[i][j]

print(answer)