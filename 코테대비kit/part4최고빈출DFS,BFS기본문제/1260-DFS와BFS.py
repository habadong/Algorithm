import sys
sys.stdin = open("예제.txt", "r")
from collections import deque

n, m, v = map(int, input().split())
visited1 = [0 for i in range(n+1)]
visited2 = [0 for i in range(n+1)]
graph = [[0] * (n + 1)for _ in range(n+1)]
answer1 = []
answer2 = []
for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = graph[b][a] = 1 # 간선 양방향

def dfs(v):
    visited1[v] = 1
    answer1.append(v)
    for i in range(1, n+1):
        if graph[v][i] == 1:
            if visited1[i] == 0:                
                dfs(i)
    
def bfs(v):
    queue = deque()
    queue.append(v)
    visited2[v] = 1
    while queue:
        v = queue.popleft()
        answer2.append(v)
        for i in range(1, n+1):
            if graph[v][i] == 1 and visited2[i] == 0:
                queue.append(i)
                visited2[i] = 1

dfs(v)
bfs(v)
print(*answer1)
print(*answer2)