import sys
sys.stdin = open("예제.txt", "r")

n = int(input())

for i in range(9):
    print(n, "*", i+1, "=", n*(i+1))