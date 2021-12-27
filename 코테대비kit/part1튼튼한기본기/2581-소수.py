import sys
sys.stdin = open("예제.txt", "r")

import math
m = int(input())
n = int(input())
arr = []

def func(a):
    if a == 1:
        return False
    elif a == 2:
        return True
    for i in range(2, a):
        if a % i == 0:
            return False
    return True

for i in range(m, n+1):
    if func(i):
        arr.append(i)

if arr:
    print(sum(arr))
    print(arr[0])
else:
    print(-1)