import sys
sys.stdin = open("예제.txt", "r")

while True:
    try:
        a, b = input().split()
        print(int(a)+int(b))
    except:
        break