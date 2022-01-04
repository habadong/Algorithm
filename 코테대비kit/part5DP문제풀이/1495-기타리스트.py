import sys
sys.stdin = open("예제.txt", "r")

## 탑다운으로 풀려다가 dp를 저장하는 방식에서 잘못 생각했음. 
## 메모이제이션을 어떻게 해야할지에 대해서 깊이 생각해봐야 할것 같다

n, s, m = map(int, input().split())
v = list(map(int, input().split()))
dp = [[-1] * (m+1) for i in range(n+1)]
dp[0][s] = 1
answer = -1
for i in range(n):
    for j in range(m+1):
        if dp[i][j] == 1:
            if j + v[i] <= m:
                dp[i+1][j+v[i]] = 1
            if j - v[i] >= 0:
                dp[i+1][j-v[i]] = 1
for i in range(m, -1, -1):
    if dp[n][i] == 1:
        answer = i
        break
print(answer)