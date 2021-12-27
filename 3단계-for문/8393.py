import sys
sys.stdin = open("예제.txt", "r")

n = int(input())
sum = 0
for i in range(n+1):
    sum += i

print(sum)