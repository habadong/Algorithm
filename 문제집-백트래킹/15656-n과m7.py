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

    for i in array:
        arr.append(i)
        func()
        arr.pop()

func()