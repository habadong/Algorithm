import sys
sys.stdin = open("예제.txt", "r")

n = int(input())
t = [0]
p = [0]
dp = [0] * (n + 2)
for i in range(n): #t,p 리스트 생성
    arr = list(map(int, sys.stdin.readline().split()))
    t.append(arr[0])
    p.append(arr[1])

for i in range(1, n+1):
    if t[i]+i <= n+1: # 현재 일수와 작업시간이 범위 안에 있을때
        # 기존 dp+작업시간 과 해당금액에서 최대이익
        dp[t[i]+i] = max(p[i]+dp[i], dp[t[i]+i]) 
    #다음날 dp는 기존반영된 금액에서의 최대이익
    dp[i+1] = max(dp[i], dp[i+1])

print(dp[-1])