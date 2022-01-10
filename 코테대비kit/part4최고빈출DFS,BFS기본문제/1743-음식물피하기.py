import sys
sys.stdin = open("예제.txt", "r")
sys.setrecursionlimit(100000)
## 음식물 덩어리들 중에서 가장 큰 음식물의 크기를 구하는 것이기 때문에 dfs

n, m, k = map(int, input().split())
matrix = [[0]*m for _ in range(n)]
visited = [[0]*m for _ in range(n)]
for i in range(k):
    data = list(map(int, input().split()))
    matrix[data[0]-1][data[1]-1] = 1
dx, dy = [-1,1,0,0],[0,0,-1,1]
answer = []
cnt = 0

def dfs(x, y):
    global cnt
    cnt += 1
    visited[x][y] = 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if matrix[nx][ny] == 1 and visited[nx][ny] == 0:
                dfs(nx, ny)
    return cnt

for i in range(n):
    for j in range(m):
        if matrix[i][j] == 1 and visited[i][j] == 0:
            answer.append(dfs(i, j))
            cnt = 0

print(max(answer))