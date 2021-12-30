import sys
sys.stdin = open("예제.txt", "r")

n = int(input())
t, p = [0], [0]
for i in range(n):
    arr = list(map(int, sys.stdin.readline().split()))
    t.append(arr[0])
    p.append(arr[1])
dp = [0] * (n+2)

for i in range(1, n+1):
    if t[i]+i <= n+1:
        dp[t[i]+i] = max(dp[i]+p[i],dp[t[i]+i])
    dp[i+1] = max(dp[i+1], dp[i])

print(dp)