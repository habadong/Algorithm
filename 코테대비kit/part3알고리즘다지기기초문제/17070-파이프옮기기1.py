import sys
sys.stdin = open("예제.txt", "r")

n = int(input())
home = [list(map(int, input().split())) for _ in range(n)]
count = 0

# 1차 풀이
def dfs2(x1, x2, y1, y2): 
    global count
    if x2 == n-1 and y2 == n-1:
        count += 1

    if x2-x1 == 0 and y2-y1 == 1: # 가로
        if y2+1 < n and home[x2][y2+1] != 1:
            dfs(x1, x2, y1+1, y2+1)
        if y2+1 < n and x2+1 <n and home[x2][y2+1] != 1 and home[x2+1][y2] != 1 and home[x2+1][y2+1] != 1:
            dfs(x1, x2+1, y1+1, y2+1)
    if x2-x1 == 1 and y2-y1 == 0: # 세로
        if x2+1 < n and home[x2+1][y2] != 1:
            dfs(x1+1, x2+1, y1, y2)
        if y2+1 < n and x2+1 <n and home[x2][y2+1] != 1 and home[x2+1][y2] != 1 and home[x2+1][y2+1] != 1:
            dfs(x1+1, x2+1, y1, y2+1)
    if x2-x1 == 1 and y2-y1 == 1: # 대각선
        if y2+1 < n and home[x2][y2+1] != 1:
            dfs(x1+1, x2, y1+1, y2+1)
        if x2+1 < n and home[x2+1][y2] != 1:
            dfs(x1+1, x2+1, y1+1, y2)
        if y2+1 < n and x2+1 <n and home[x2][y2+1] != 1 and home[x2+1][y2] != 1 and home[x2+1][y2+1] != 1:
            dfs(x1+1, x2+1, y1+1, y2+1)

dfs2(0,0,0,1)
print(count)


#2차 풀이
def dfs1(x, y, shape): 
    global count
    if x == n-1 and y == n-1:
        count += 1
    if shape == 0: 
        if y+1 < n and home[x][y+1] != 1:
            dfs(x, y+1, 0)
        if y+1 < n and x+1 < n:
            if home[x+1][y+1] != 1 and home[x+1][y] != 1 and home[x][y+1] != 1:
                dfs(x+1, y+1, 2)
    elif shape == 1:
        if x+1 < n and home[x+1][y] != 1:
            dfs(x+1, y, 1)
        if y+1 < n and x+1 < n:
            if home[x+1][y+1] != 1 and home[x+1][y] != 1 and home[x][y+1] != 1:
                dfs(x+1, y+1, 2)
    elif shape == 2:
        if x+1 < n and home[x+1][y] != 1:
            dfs(x+1, y, 1)
        if y+1 < n and home[x][y+1] != 1:
            dfs(x, y+1, 0)
        if y+1 < n and x+1 < n:
            if home[x+1][y+1] != 1 and home[x+1][y] != 1 and home[x][y+1] != 1:
                dfs(x+1, y+1, 2)

dfs1(0,1,0)
print(count)