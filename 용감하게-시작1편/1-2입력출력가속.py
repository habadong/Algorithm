import sys
sys.stdin = open("예제.txt", "r")

N = int(sys.stdin.readline())
sys.stdout.write(N)

from sys import stdin, stdout
input = stdin.readline
print = stdout.write