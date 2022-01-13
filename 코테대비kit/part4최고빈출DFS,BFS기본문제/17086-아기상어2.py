import sys
sys.stdin = open("예제.txt", "r")
from collections import deque

n, m = map(int, input().split())
graph = []
answer = []
for i in range(n):
    arr = list(map(int, input().split()))
    graph.append(arr)
dx = [-1, 0, 1, 1, 1, 0, -1, -1] # 좌상, 좌, 좌하, 하, 우하, 우, 우상, 상
dy = [-1, -1, -1, 0, 1, 1, 1, 0] # 좌상, 좌, 좌하, 하, 우하, 우, 우상, 상

def bfs(x,y):
    visited = [[0]*m for _ in range(n)]
    queue = deque()
    queue.append([x,y])
    visited[x][y] = 1
    while queue:
        a, b = queue.popleft()
        for i in range(8):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 1:
                    return visited[a][b]
                if visited[nx][ny] == 0:
                    visited[nx][ny] = visited[a][b] + 1
                    queue.append([nx,ny])

for i in range(n):
    for j in range(m):
        if graph[i][j] != 1:
            answer.append(bfs(i,j))

print(max(answer))