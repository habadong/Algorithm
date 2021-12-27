import sys
sys.stdin = open("예제.txt", "r")

n = int(sys.stdin.readline().rstrip())

for i in range(1, n+1):
    print(i)