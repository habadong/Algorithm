import sys
sys.stdin = open("예제.txt", "r")

n, m = map(int, input().split())
array = list(map(int, input().split()))
array.sort()

arr = []

def func():
    if len(arr) == m:
        print(*arr)
        return

    for i in range(n):
        if array[i] not in arr:
            arr.append(array[i])
            func()
            arr.pop()

func()