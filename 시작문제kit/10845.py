import sys
sys.stdin = open("예제.txt", "r")

n = int(sys.stdin.readline())
q = []

for i in range(n):
    order = sys.stdin.readline().rstrip()
    
    if order == 'pop':
        if len(q) == 0:
            print(-1)
        else:
            print(q.pop(0))
    elif order == 'size':
        print(len(q))
    elif order == 'empty':
        if len(q) == 0:
            print(1)
        else:
            print(0)
    elif order == 'front':
        if len(q) == 0:
            print(-1)
        else:
            print(q[0])
    elif order == 'back':
        if len(q) == 0:
            print(-1)
        else:
            print(q[len(q)-1])
    else:
        num = order.split()[1]
        q.append(num)