import sys
sys.stdin = open("예제.txt", "r")

n = int(input())
arr = list(map(int, sys.stdin.readline().split()))
print(str(min(arr))+" "+str(max(arr)))
