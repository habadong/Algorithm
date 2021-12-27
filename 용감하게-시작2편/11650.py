import sys
sys.stdin = open("예제.txt", "r")

n = int(input())
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))

arr.sort(key=lambda x: (x[0], x[1]))

for i in range(n):
    print(*arr[i])