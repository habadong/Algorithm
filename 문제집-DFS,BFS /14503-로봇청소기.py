import sys
sys.stdin = open("예제.txt", "r")

n, m = map(int, input().split())
r, c, d = map(int, input().split())
graph = [list(map(int, input().split())) for i in range(n)]
visited = [[0] * (m) for i in range(n)]
rotate = [[3,2,1,0],[0,3,2,1],[1,0,3,2],[2,1,0,3]]
dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]
answer = 0

def dfs(r, c, direction):
    global answer
    if visited[r][c] == 0:
        visited[r][c] = 1
        answer += 1
    for i in rotate[direction]:
        nx = r + dx[i]
        ny = c + dy[i]            
        if graph[nx][ny] != 1 and visited[nx][ny] == 0:
            direction = i
            dfs(nx, ny, direction)
            return

    bx = r + (-1 * dx[direction])
    by = c + (-1 * dy[direction])
    if graph[bx][by] == 1:
        return
    dfs(bx, by, direction)

dfs(r,c,d)
print(answer)