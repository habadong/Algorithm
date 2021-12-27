import sys
sys.stdin = open("예제.txt", "r")
from collections import deque

n, k = map(int, input().split())
MAX = 100000
queue = deque([n])
dist = [0] * (MAX+1)

while queue:

    v = queue.popleft()

    if v == k:
        print(dist[v])
        break
    for i in (v-1, v+1, v*2):
        if 0 <= i <= MAX and not dist[i]:
            dist[i] = dist[v] + 1
            queue.append(i)