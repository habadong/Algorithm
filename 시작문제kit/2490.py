import sys
sys.stdin = open("예제.txt", "r")

for i in range(3):
    a = input().split()
    num = a.count('1')

    if num == 0:
        print("D")
    elif num == 1:
        print("C")
    elif num == 2:
        print("B")
    elif num == 3:
        print("A")
    elif num == 4:
        print("E")

