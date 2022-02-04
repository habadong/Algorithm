import sys
sys.stdin = open("예제.txt", "r")
from collections import deque

n, m = map(int, input().split())
graph = [list(map(int, sys.stdin.readline().split())) for i in range(n)]
answer = 0
result = False
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(r, c):
    queue = deque()
    queue.append([r,c])
    visited[r][c] = 1
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if graph[nx][ny] == 0:
                count[x][y] += 1
            if graph[nx][ny] != 0 and visited[nx][ny] == 0:
                queue.append([nx, ny])
                visited[nx][ny] = 1

while 1:
    check = 0
    visited = [[0]*m for i in range(n)]
    count = [[0]*m for i in range(n)]
    for i in range(1, n-1):
        for j in range(1, m-1):
            if graph[i][j] != 0 and visited[i][j] == 0:
                bfs(i, j)
                check += 1

    for i in range(1, n-1):
        for j in range(1, m-1):
            if graph[i][j] < count[i][j]:
                graph[i][j] = 0 
            else:
                graph[i][j] = graph[i][j] - count[i][j]

    if check >= 2:
        result = True
        break
    if check == 0:
        break
    answer += 1

if result:
    print(answer)
else:
    print(0)