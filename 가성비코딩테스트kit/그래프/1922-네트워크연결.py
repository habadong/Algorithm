import sys
sys.stdin = open("예제.txt", "r")

n = int(input())
m = int(input())
edge = []
answer = 0

parent = [0] * (n+1) # 부모테이블 초기화
for i in range(1, n+1): #부모테이블을 자기 자신으로 초기화
    parent[i] = i

def find(parent, x):
    # 루트 노드를 찾을때까지 재귀적으로 반복
    if parent[x] == x:
        return x
    parent[x] = find(parent, parent[x])
    return parent[x]

# 두 원소가 속한 집합 찾기, 간선을 연결 
def union(parent, a, b):
    A = find(parent, a)
    B = find(parent, b)

    if A < B:
        parent[B] = A
    else:
        parent[A] = B


for i in range(m):
    a, b, cost = map(int, input().split())
    edge.append((cost, a, b))

# 1. 간선들을 비용 기준으로 오름차순으로 정렬한다.
edge.sort()

for i in range(m):
    cost, a, b = edge[i]
    # 사이클을 발생시키지 않는 간선일 경우에만 연결한다
    if find(parent, a) != find(parent, b):
        union(parent, a, b)
        answer += cost

print(answer)

