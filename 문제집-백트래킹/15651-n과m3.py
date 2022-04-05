import sys
sys.stdin = open("예제.txt", "r")

n, m = map(int, input().split())
array = []

def func():
    if len(array) == m:
        print(*array)
        return

    for i in range(1, n+1):
        array.append(i)
        func()
        array.pop()

func()