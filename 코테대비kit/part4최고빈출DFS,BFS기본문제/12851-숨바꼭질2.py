import sys
sys.stdin = open("예제.txt", "r")
from collections import deque

n, k = map(int, input().split())
MAX = 100001
queue = deque()
queue.append(n)
visited = [-1] * MAX
visited[n] = 0
count = 0

while queue:
    v = queue.popleft()
    if v == k:
        count += 1
    for i in [v*2, v+1, v-1]:
        if 0 <= i < MAX:
            # 방문한적이 없거나 이전에 계산되어 방문했고 현재시간+1 인 경우
            if visited[i] == -1 or visited[i] >= visited[v] + 1:
                visited[i] = visited[v] + 1
                queue.append(i)
                

print(visited[k])
print(count)