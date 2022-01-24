import sys
sys.stdin = open("예제.txt", "r")
from collections import deque

m, n, h = map(int, input().split())
graph = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]
# 익은 토마토 1, 익지 않은 토마토 0, 토마토가 없는 칸 -1
# 상 , 하 , 좌 , 우 , 전 , 후
dx = [0, 0, -1, 1, 0, 0]
dy = [0, 0, 0, 0, -1, 1]
dz = [1, -1, 0, 0, 0, 0]
visited = [[[0 for _ in range(m)] for _ in range(n)] for _ in range(h)]
queue = deque()
answer = 0
def bfs():
    while queue:
        c, b, a = queue.popleft()
        visited[c][b][a] = 1
        for i in range(6):
            nx = a + dx[i]
            ny = b + dy[i]
            nz = c + dz[i]
            if 0 <= nz < h and 0 <= ny < n and 0 <= nx < m:
                # if visited[nz][ny][nx] == 0 and graph[nz][ny][nx] == 1:
                #     queue.append([nz, ny, nx])
                #     visited[nz][ny][nx] = 1
                if visited[nz][ny][nx] == 0 and graph[nz][ny][nx] == 0:
                    queue.append([nz, ny, nx])
                    visited[nz][ny][nx] = 1
                    graph[nz][ny][nx] = graph[c][b][a] + 1
                    # tomato0.append([nz, ny, nx])


for i in range(h):
    for j in range(n):
        for k in range(m):
            if graph[i][j][k] == 1:
                queue.append([i,j,k])
bfs()

result = -1
for i in range(h):
    for j in range(n):
        for k in range(m):
            if graph[i][j][k] == 0:
                answer = -1
            result = max(result, graph[i][j][k])

if answer == -1:
    print(answer)
elif result != -1:
    print(result-1)