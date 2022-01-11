import sys
sys.stdin = open("예제.txt", "r")

a, b = map(int, input().split())
answer = -1

def dfs(num, depth):
    global answer
    if num == b:
        answer = depth
    if num * 2 <= b:
        dfs(num*2, depth+1)
    if int(str(num)+'1') <= b:
        dfs(int(str(num)+'1'), depth+1)

dfs(a, 1)
print(answer)