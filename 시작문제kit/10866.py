import sys
sys.stdin = open("예제.txt", "r")

n = int(sys.stdin.readline())
d = []

for i in range(n):
    order = sys.stdin.readline().rstrip()
    
    if order == 'pop_front':
        if len(d) == 0:
            print(-1)
        else:
            print(d.pop(0))
    elif order == 'pop_back':
        if len(d) == 0:
            print(-1)
        else:
            print(d.pop())
    elif order == 'size':
        print(len(d))
    elif order == 'empty':
        if len(d) == 0:
            print(1)
        else:
            print(0)
    elif order == 'front':
        if len(d) == 0:
            print(-1)
        else:
            print(d[0])
    elif order == 'back':
        if len(d) == 0:
            print(-1)
        else:
            print(d[len(d)-1])
    else:
        push, x = map(str, order.split())
        if push == 'push_front':
            d.insert(0, x)
        elif push == 'push_back':
            d.append(x)