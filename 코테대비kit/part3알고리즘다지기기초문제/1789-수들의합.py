import sys
sys.stdin = open("예제.txt", "r")

s = int(input())
n = 1

while (n*(n+1))/2 <= s:
    n += 1

print(n-1)