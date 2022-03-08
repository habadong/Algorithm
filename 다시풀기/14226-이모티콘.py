import sys
sys.stdin = open("예제.txt", "r")
from collections import deque

n = int(input())

dic = dict()
queue = deque()

dic[(1, 0)] = 0
queue.append([1, 0])

while queue:
    s, clip = queue.popleft()

    if s == n:
        print(dic[(s, clip)])
        break

    if (s, s) not in dic.keys():
        dic[(s, s)] = dic[(s, clip)] + 1
        queue.append([s, s])
    if (s+clip, clip) not in dic.keys():
        dic[(s+clip, clip)] = dic[(s, clip)] + 1
        queue.append([s+clip, clip])
    if (s-1, clip) not in dic.keys():
        dic[(s-1, clip)] = dic[(s, clip)] + 1
        queue.append([s-1, clip])
      