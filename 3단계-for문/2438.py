import sys
sys.stdin = open("예제.txt", "r")

n = int(input())

for i in range(1, n+1):
    star = ""
    for j in range(i):
        star += "*"
    print(star)
    