import sys
sys.stdin = open("예제.txt", "r")

n = int(input())
arr = [list(input()) for _ in range(n)]
MAX = 0

def check_function(a, b):
    c = ''
    r = ''
    c_MAX = 0
    r_MAX = 0
    count = 0
    for i in range(n):
        for j in range(n):
            if c != arr[i][j]:
                c = arr[i][j]
                count = 1
            else:
                count += 1
                c_MAX = max(c_MAX, count)
        count = 0
        c = ''

        for j in range(n):
            if r != arr[j][i]:
                r = arr[j][i]
                count = 1
            else:
                count += 1
                r_MAX = max(r_MAX, count)
        count = 0 
        r = ''
    return max(c_MAX, r_MAX)

for i in range(n):
    for j in range(n):
        MAX = max(check_function(i, j), MAX)
        if j+1 < n and arr[i][j] != arr[i][j+1]:
            arr[i][j], arr[i][j+1] = arr[i][j+1], arr[i][j]
            MAX = max(check_function(i, j), MAX)
            arr[i][j], arr[i][j+1] = arr[i][j+1], arr[i][j]
        if i+1 < n and arr[i][j] != arr[i+1][j]:
            arr[i][j], arr[i+1][j] = arr[i+1][j], arr[i][j]
            MAX = max(check_function(i, j), MAX)
            arr[i][j], arr[i+1][j] = arr[i+1][j], arr[i][j]

print(MAX)