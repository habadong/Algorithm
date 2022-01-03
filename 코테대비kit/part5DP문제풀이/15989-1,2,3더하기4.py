import sys
sys.stdin = open("예제.txt", "r")

t = int(input())
dp = [1 for i in range(10001)]

for i in range(2, 10001):
    dp[i] += dp[i-2]
for i in range(3, 10001):
    dp[i] += dp[i-3]

for i in range(t):
    print(dp[int(input())])