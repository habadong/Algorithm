import sys
sys.stdin = open("예제.txt", "r")

a = list(sys.stdin.readline().rstrip())
b = list(sys.stdin.readline().rstrip())
length_a = len(a)
length_b = len(b)

dp = [[0]*(length_a+1) for i in range(length_b+1)]

for i in range(1, length_b+1):
    for j in range(1, length_a+1):
        if b[i-1] == a[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        elif b[i-1] != a[j-1]:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(dp[-1][-1])