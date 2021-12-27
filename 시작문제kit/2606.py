import sys
sys.stdin = open("예제.txt", "r")
from collections import deque

n = int(input())
m = int(input())
answer = 0
graph = [[] * (n+1) for _ in range(n+1)]
visited = [0] * (n+1)
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(node):
    global answer
    queue = deque([node])    
    visited[node] = 1
    while queue:
        a = queue.popleft()
        
        for i in graph[a]:
            if visited[i] == 0:
                queue.append(i)
                visited[i] = 1
                answer += 1
bfs(1)
print(answer)
