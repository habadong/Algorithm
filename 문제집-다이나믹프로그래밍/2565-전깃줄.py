import sys
sys.stdin = open("예제.txt", "r")

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
dp = [1] * n

graph.sort()

for i in range(n):
    for j in range(i):
        if graph[j][1] < graph[i][1]:
            dp[i] = max(dp[i], dp[j]+1)

print(n-max(dp))