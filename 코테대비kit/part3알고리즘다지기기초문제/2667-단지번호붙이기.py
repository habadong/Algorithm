import sys
sys.stdin = open("예제.txt", "r")

n = int(input())
graph = [list(map(int, input())) for i in range(n)]
count = 0
answer = []

def dfs(x, y):
    global count
    graph[x][y] = 0
    count += 1
    if x-1 >= 0 and graph[x-1][y] == 1:
            dfs(x-1, y)
    if x+1 < n and graph[x+1][y] == 1:
            dfs(x+1, y)
    if y-1 >= 0 and graph[x][y-1] == 1:
            dfs(x, y-1)
    if y+1 < n and graph[x][y+1] == 1:
            dfs(x, y+1)

    return count


for i in range(n):
    for j in range(n):
        if graph[i][j]:
            answer.append(dfs(i, j))
            count = 0
    
answer.sort()
print(len(answer))
for i in answer:
    print(i)