import sys
sys.stdin = open("예제.txt", "r")
from collections import deque

s = int(input())
graph = [[-1]*(s+1) for _ in range(s+1)]
queue = deque()
queue.append([1,0]) ## [화면에 있는 이모티콘 개수, 클립보드에 저장되 있는 이모티콘 개수]
graph[1][0] = 0

while queue:
    screen, clip = queue.popleft()

    if screen == s:
        print(graph[s][clip])
        break
    ## 화면 이모티콘 개수와 그 때의 클립보드에 있는 이모티콘의 개수를 같이 저장해야한다
    # 이모티콘 복사하는 경우, 같은 개수에서 또 복사 하지 않은 경우
    if graph[screen][screen] == -1: 
        graph[screen][screen] = graph[screen][clip] + 1
        queue.append([screen,screen])
    # 클립보드의 개수를 화면에 더하는 경우, 클립보드의 개수는 복사하지 않았으니 그대로 유지된다
    if screen+clip <= s and graph[screen+clip][clip] == -1:
        graph[screen+clip][clip] = graph[screen][clip] + 1
        queue.append([screen+clip, clip])
    # 화면에 있는 이모티콘 하나를 지우는 경우, 마찬가지로 클립보드에 복사하지 않았으니 그대로 유지
    if screen-1 >= 1 and graph[screen-1][clip] == -1:
        graph[screen-1][clip] = graph[screen][clip] + 1
        queue.append([screen-1, clip])
    




## 클립 보드를에 저장되는 경우를 이전과 현재를 알고 있어야 하기 때문에 
## 클립보드를 하나만 두는것은 실패함
# while queue:
#     v = queue.popleft()

#     if v == s:
#         break

#     for i in ['copy', 'paste', 'delete']:
#         if i == 'copy':
#             buffer = v
#             visited[v] += 1
#             queue.append(v)
#         elif i == 'paste':
#             if buffer != 0 and v+buffer < MAX:
#                 x = v+buffer
#                 visited[x] = visited[v] + 1
#                 queue.append(x)
#         elif i == 'delete':
#             if 1 <= v-1:
#                 x = v-1
#                 visited[x] = visited[v] + 1
#                 queue.append(x)