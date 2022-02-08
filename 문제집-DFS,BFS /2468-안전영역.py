import sys
sys.stdin = open("예제.txt", "r")
from collections import deque

n = int(input())
graph = [list(map(int, input().split())) for i in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
rain = 0
safe = 1

def map_func(x):
    global check, result
    if 0 < x <= rain:
        check = True
        return -1
    else:
        return x

def bfs(a, b):
    queue = deque()
    queue.append([a, b])
    visited[a][b] = 1

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if visited[nx][ny] == 0 and graph[nx][ny] != -1:
                    queue.append([nx, ny])
                    visited[nx][ny] = 1

while 1:
    check = False
    result = False
    rain += 1
    for i in range(n):
        graph[i] = list(map(map_func, graph[i]))    

    if check == True:
        visited = [[0] * n for i in range(n)]
        count = 0
        for i in range(n):
            for j in range(n):
                if visited[i][j] == 0 and graph[i][j] != -1:
                    bfs(i, j)
                    count += 1

        safe = max(count, safe)

    for i in range(n):
        for j in range(n):
            if graph[i][j] > 0:
                result = True
    
    if result == False:
        break

print(safe)