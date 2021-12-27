import sys
sys.stdin = open("예제.txt", "r")

t = int(input())
for i in range(t):
    s = " ".join(list(map(lambda a: a[::-1],sys.stdin.readline().rstrip().split())))
    print(s)