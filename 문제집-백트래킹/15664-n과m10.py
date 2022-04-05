import sys
sys.stdin = open("예제.txt", "r")

n, m = map(int, input().split())
array = list(map(int, input().split()))
array.sort()
arr = []
isused = [0] * n

def func(k):
    store = 0
    if len(arr) == m:
        print(*arr)
        return 
    for i in range(k, n):
        if isused[i] == 0 and store != array[i]:
            arr.append(array[i])
            isused[i] = 1
            store = array[i]
            func(i+1)
            arr.pop()
            isused[i] = 0

func(0)
