import sys
sys.stdin = open("예제.txt", "r")

t = int(input())
dp = [-1] * 1000001
dp[1] = 1
dp[2] = 2
dp[3] = 4

for i in range(4, 1000001):
    dp[i] = (dp[i-1] + dp[i-2] + dp[i-3]) % 1000000009
    # 오버플로우 문제로 인해 리스트에 올바른 값이 저장되지 않아 10억으로 나눠야함
for _ in range(t):
    print(dp[int(input())])