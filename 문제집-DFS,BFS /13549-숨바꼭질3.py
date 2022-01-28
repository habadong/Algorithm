import sys
sys.stdin = open("예제.txt", "r")
from collections import deque

n, k = map(int, input().split())
MAX = 100001
visited = [-1] * MAX
queue = deque()
queue.append(n)
visited[n] = 0

while queue:
    v = queue.popleft()
    if v == k:
        break
    if 0 <= v*2 < MAX and visited[v*2] == -1:
        queue.appendleft(v*2)
        visited[v*2] = visited[v]
    if 0 <= v+1 < MAX and visited[v+1] == -1:
        queue.append(v+1)
        visited[v+1] = visited[v] + 1
    if 0 <= v-1 < MAX and visited[v-1] == -1:
        queue.append(v-1)
        visited[v-1] = visited[v] + 1

print(visited[k])