import sys
sys.stdin = open("예제.txt", "r")

n, m = map(int, input().split())
array = list(map(int, input().split()))
array.sort()
arr = []

def func(k):
    store = 0
    if len(arr) == m:
        print(*arr)
        return

    for i in range(k, n):
        if store != array[i]:
            arr.append(array[i])
            store = array[i]
            func(i)
            arr.pop()

func(0)