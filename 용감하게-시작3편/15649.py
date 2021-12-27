import sys
sys.stdin = open("예제.txt", "r")

from itertools import permutations

n, m = map(int, input().split())

arr = [str(i+1) for i in range(n)]

for i in list(permutations(arr, m)):
    print(" ".join(i))