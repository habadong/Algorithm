def solution(triangle):
    answer = 0
    n = len(triangle)
    dp = [[0]*(n+2) for _ in range(n+1)]
    dp[1][1] = triangle[0][0]

    for i in range(2, n+1):
        for j in range(1, i+1):
            if j < n:
                dp[i][j] = max(dp[i-1][j-1]+triangle[i-1][j-1], dp[i-1][j]+triangle[i-1][j-1])

    answer = max(dp[n])
    return answer