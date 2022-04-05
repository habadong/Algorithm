import sys
sys.stdin = open("예제.txt", "r")

n, m = map(int, input().split())
array = []

def func(k):
    if len(array) == m:
        print(*array)
        return

    for i in range(k, n+1):
        array.append(i)
        func(i)
        array.pop()

func(1)