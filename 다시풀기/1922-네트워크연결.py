import sys
sys.stdin = open("예제.txt", "r")

## union - find 알고리즘 

def find(parent, x):
    if parent[x] == x:
        return x
    parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    root_a = find(parent, a)
    root_b = find(parent, b)

    if root_a < root_b:
        parent[root_b] = root_a
    else:
        parent[root_a] = root_b

n = int(input()) ## number of computer
m = int(input()) ## number of network
graph = []

## 간선을 담을 parent 와 최종 답 answer
parent = [0] * (n + 1)
answer = 0

# 리스트를 자기 자신으로 초기화 시켜줌
for i in range(n+1):
    parent[i] = i

for i in range(m):
    graph.append(list(map(int, input().split())))

graph.sort(key=lambda x: x[2])

for i in graph:
    a, b, cost = i
    if find(parent, a) != find(parent, b): ## 사이클이 없을때
        union(parent, a, b)
        answer += cost

print(answer)
