import sys
sys.stdin = open("예제.txt", "r")

n = int(sys.stdin.readline().rstrip())

for i in range(n):
    a, b = sys.stdin.readline().rstrip().split()
    print(int(a) + int(b))