import sys
sys.stdin = open("예제.txt", "r")

n, m = map(int, input().split())
array = list(map(int, input().split()))
array.sort()
arr = []
isused = [0] * n

def func():
    store = 0
    if len(arr) == m:
        print(*arr)
        return

    for i in range(n):
        if store != array[i]:
            arr.append(array[i])
            # isused[i] = 1
            store = array[i]
            func()
            # isused[i] = 0
            arr.pop()

func()