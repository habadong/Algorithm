import sys
sys.stdin = open("예제.txt", "r")
from collections import deque

n = int(input())
graph = [list(map(int, input())) for i in range(n)]
visited = []
answer = []

def bfs(x, y):
    dx = [1, -1, 0, 0] #좌우 좌표
    dy = [0, 0, 1, -1] #상하 좌표
    count = 0
    queue = deque() #bfs를 위한 큐 생성

    # 큐에 집이있는 정점을 넣는다
    queue.append((x, y))

    graph[x][y] = 0
    visited.append((x, y))

    while queue:
        now = queue.popleft()
        count += 1
        
        for i in range(4):
            nx = now[0] + dx[i]
            ny = now[1] + dy[i]

            # 상하좌우 좌표가 0과 n의 범위안에 있을때
            if 0<=nx<n and 0<=ny<n:
                # 집이 있고 방문하지 않았다면
                if graph[nx][ny] == 1 and (nx, ny) not in visited:
                    # 1을 0으로 처리하여 제외시킴
                    graph[nx][ny] = 0
                    queue.append((nx,ny))
                    visited.append((nx, ny))
    return count


for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            answer.append(bfs(i,j))

answer.sort()
print(len(answer))
for i in answer:
    print(i)