import sys
sys.stdin = open("예제.txt", "r")

n = int(input())
graph = [list(map(int, input().split())) for i in range(n)]
dp = [[0]*(n+2) for i in range(n+1)]
dp[1][1] = graph[0][0]

for i in range(2, n+1):
    for j in range(1, i+1):
        dp[i][j] = max(dp[i-1][j-1] + graph[i-1][j-1], dp[i-1][j]+ graph[i-1][j-1])

print(max(dp[n]))