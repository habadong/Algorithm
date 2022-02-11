import sys
sys.stdin = open("예제.txt", "r")
from collections import deque

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for i in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
answer = 0

def spread_virus():
    global answer
    virus = deque()
    result = 0
    copy = [[0]*m for i in range(n)]
    for i in range(n):
        for j in range(m):
            copy[i][j] = graph[i][j]

    for i in range(n):
        for j in range(m):
            if copy[i][j] == 2:
                virus.append([i, j])

    while virus:
        x, y = virus.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if copy[nx][ny] == 0:
                    copy[nx][ny] = 2
                    virus.append([nx, ny])

    for i in range(n):
        for j in range(m):
            if copy[i][j] == 0:
                result += 1

    answer = max(result, answer)
    
def wall(count):
    if count == 3:
        spread_virus()
        return
        
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0: #이런식의 재귀적 진행은 알아둬야겠다
                graph[i][j] = 1
                wall(count+1)
                graph[i][j] = 0

wall(0)
print(answer)