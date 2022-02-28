import sys
sys.stdin = open("예제.txt", "r")
from collections import deque

# 상, 상우, 우, 하우, 하, 하좌, 좌, 상좌
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

def bfs(a, b):
    global w, h
    queue = deque()
    queue.append([a, b])
    visited[a][b] = 1
    
    while queue:
        x, y = queue.popleft()

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < h and 0 <= ny < w:
                if graph[nx][ny] == 1 and visited[nx][ny] == 0:
                    queue.append([nx, ny])
                    visited[nx][ny] = 1

while True:
    w, h = map(int, input().split())
    graph = []
    visited = [[0] * w for _ in range(h)]
    answer = 0
    if w == 0 and h == 0:
        break

    for i in range(h):
        graph.append(list(map(int, input().split())))

    for i in range(h):
        for j in range(w):
            if graph[i][j] == 1 and visited[i][j] == 0:
                bfs(i, j)
                answer += 1
    
    print(answer)
