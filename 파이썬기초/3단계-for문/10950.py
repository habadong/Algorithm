import sys
sys.stdin = open("예제.txt", "r")

n = int(input())

for i in range(n):
    a, b = input().split()
    print(int(a) + int(b))