import sys
sys.stdin = open("예제.txt", "r")
from collections import deque

def pop_puyo():
    for i in range(6):
        for j in range(10, -1, -1):            
            for k in range(11, j, -1):
                if graph[j][i] != "." and graph[k][i] == ".":
                    graph[k][i] = graph[j][i]
                    graph[j][i] = "."
                    break

def bfs(a, b, color):
    queue = deque()
    queue.append([a,b])
    count.append([a,b])
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < 12 and 0 <= ny < 6:
                if visited[nx][ny] == 0 and graph[nx][ny] == color:
                    queue.append([nx, ny])
                    visited[nx][ny] = 1
                    count.append([nx,ny])

graph = [list(map(str, input())) for i in range(12)]

# 좌우상하 리스트
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
answer = 0

while True:
    breaking = False
    visited = [[0] * 6 for _ in range(12)]

    for i in range(12):
        for j in range(6):
            if graph[i][j] != "." and visited[i][j] == 0:
                visited[i][j] = 1
                count = []
                bfs(i, j, graph[i][j])
                if len(count) >= 4:
                    breaking = True
                    for i in range(len(count)):
                        graph[count[i][0]][count[i][1]] = "."
    if breaking == False:
        break
    pop_puyo()
    answer += 1

print(answer)

## 1차 시도
'''
graph = [list(map(str, input())) for i in range(r)]
# 방문 여부 초기화
visited = [list(map(lambda x: -1 if x == "." else 0, graph[i])) for i in range(r)]

def bfs(a, b):
    queue = deque()
    queue.append([a,b])
    visited[a][b] = -1
    count = [[a,b]]
    while queue:
        x, y = queue.popleft()
        color = graph[x][y]
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < r and 0 <= ny < c:
                if visited[nx][ny] == 0 and graph[nx][ny] == color:
                    queue.append([nx, ny])
                    visited[nx][ny] = -1
                    count.append([nx,ny])
    if len(count) >= 4:

for i in range(c):
    if visited[-1][i] == 0:
        print(graph[-1][i])
        break
'''