import sys
sys.stdin = open("예제.txt", "r")
from collections import deque

n, m = map(int, input().split())
matrix = [list(input()) for _ in range(n)]
visited = [[0]*m for _ in range(n)]
queue = deque()
# 맵 또는 미로에서 자주 쓰이는 좌표 리스트를 만들어서 풀어보자
# 좌, 우, 상, 하 를 표현한 리스트
dx, dy = [-1,1,0,0], [0,0,-1,1]
queue.append([0,0])
visited[0][0] = 1
while queue:
    x, y = queue.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny <m:
            if visited[nx][ny] == 0 and matrix[nx][ny] == '1':
                visited[nx][ny] = visited[x][y] + 1
                queue.append([nx, ny])

print(visited[n-1][m-1])