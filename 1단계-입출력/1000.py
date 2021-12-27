import sys
sys.stdin = open("예제.txt", "r")

N = input().split()
print(int(N[0]) * int(N[1]))