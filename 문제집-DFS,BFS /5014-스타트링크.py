import sys
sys.stdin = open("예제.txt", "r")
from collections import deque

f, s, g, u, d = map(int, input().split())
visited = [-1] * 1000001
queue = deque()
answer = -1
queue.append(s)
visited[s] = 0

while queue:
    v = queue.popleft()
    if v == g:
        answer = visited[g]
        break
    if 0<v+u<=f and visited[v+u] == -1:
        queue.append(v+u)
        visited[v+u] = visited[v] + 1
    if 0<v-d<=f and visited[v-d] == -1:
        queue.append(v-d)
        visited[v-d] = visited[v] + 1

if answer == -1:
    print("use the stairs")
else:
    print(answer)