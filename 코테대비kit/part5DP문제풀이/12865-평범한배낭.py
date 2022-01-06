import sys
sys.stdin = open("예제.txt", "r")
## 핵심 아이디어: 물품 가지수와 무게별로 가치의 최대값을 계산한다
n, k = map(int, input().split())
w, v = [0], [0]
for i in range(n):
    data = list(map(int,input().split()))
    w.append(data[0])
    v.append(data[1])
dp = [[0]*(k+1) for i in range(n+1)]

for i in range(1, n+1):
    for j in range(1, k+1):
        # 현재 넣을려는 물건의 무게가 가방보다 작으면 그전 값을 가져온다
        if j < w[i]:
            dp[i][j] = dp[i-1][j]
        # 현재 물건의 가치 + (가방-현재물건)에 들어가는 물건의 최대 가치와 이전 최대가치 중 최대값
        else:
            dp[i][j] = max(v[i]+dp[i-1][j-w[i]], dp[i-1][j])

print(dp[n][k])

