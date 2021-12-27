import sys
sys.stdin = open("예제.txt", "r")

t = int(input())
for i in range(t):
    arr = list(map(int, input().split()))
    arr.sort()
    print(arr[-3])