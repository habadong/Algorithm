import sys
sys.stdin = open("예제.txt", "r")
from collections import deque

n, m = map(int, input().split())
graph = [list(map(str, input().rstrip())) for i in range(m)]
visited = [[0] * n for i in range(m)]

# 상, 하, 좌. 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
w, b = 0, 0

def bfs(a, b, color):
    queue = deque()
    queue.append([a,b])
    result = 1
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < m and 0 <= ny < n:
                if visited[nx][ny] == 0 and graph[nx][ny] == color:
                    queue.append([nx, ny])
                    visited[nx][ny] = 1
                    result += 1
    return result

for i in range(m):
    for j in range(n):
        if visited[i][j] == 0:
            visited[i][j] = 1
            if graph[i][j] == "W":
                w += bfs(i,j,graph[i][j]) ** 2   
            else:
                b += bfs(i,j,graph[i][j]) ** 2
print(w, b)