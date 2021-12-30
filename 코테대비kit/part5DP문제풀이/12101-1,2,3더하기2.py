import sys
sys.stdin = open("예제.txt", "r")

n, k = map(int, input().split())
dp = [[] for _ in range(11)]
dp[1].append('1')
dp[2].append('1+1')
dp[2].append('2')
dp[3].append('1+1+1')
dp[3].append('1+2')
dp[3].append('2+1')
dp[3].append('3')

for i in range(4, n+1):
    for p in range(1, 4):
        for j in range(len(dp[i-p])):
            dp[i].append(str(p) + '+' + dp[i-p][j])
        
try:
    print(dp[n][k-1])
except:
    print(-1)