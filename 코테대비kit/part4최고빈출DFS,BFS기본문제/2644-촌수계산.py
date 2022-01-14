import sys
sys.stdin = open("예제.txt", "r")

n = int(input())
A, B = map(int, input().split())
m = int(input())
graph = [[] for i in range(n+1)]
visited = [0] * (n+1)
answer = 0
for i in range(m):
    arr = list(map(int, input().split()))
    graph[arr[0]].append(arr[1])
    graph[arr[1]].append(arr[0])

def dfs(node, goal, depth):
    global answer
    visited[node] = 1
    if node == goal:
        answer = depth
        return
    for v in graph[node]:
        if visited[v] == 0:
            dfs(v, goal, depth+1)
    
dfs(A, B, 0)

if answer == 0:
    print(-1)
else:
    print(answer)