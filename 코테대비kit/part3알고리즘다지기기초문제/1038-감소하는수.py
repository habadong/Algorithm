import sys
sys.stdin = open("예제.txt", "r")
from itertools import combinations

n = int(input())
arr = []
for i in range(1,11):
    for j in combinations(range(0,10), i):
        j = list(j)
        j.sort(reverse=True)
        arr.append(int("".join(map(str, j))))

arr.sort()

try:
    print(arr[n])
except:
    print(-1)