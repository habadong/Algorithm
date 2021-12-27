import sys
sys.stdin = open("예제.txt", "r")

n = int(sys.stdin.readline())
s = []

for i in range(n):
    order = sys.stdin.readline().strip()

    if order == 'top':
        if len(s) == 0:
            print("-1")
        else:
            print(s[len(s)-1])
    elif order == 'size':
        print(len(s))
    elif order == 'empty':
        if len(s) == 0:
            print("1")
        else:
            print("0")
    elif order == 'pop':
        if len(s) == 0:
            print("-1")
        else:
            print(s.pop())
    else:
        num = order.split()[1]
        s.append(num)