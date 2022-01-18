import sys
sys.stdin = open("예제.txt", "r")

a, b = input().split()

while int(a) != 0:
    if int(b) != 0:
        print(int(a)+int(b))
    a, b = input().split()