import sys
sys.stdin = open("예제.txt", "r")

n = int(input())

for i in range(n, 0, -1):
    print(i)