import sys
sys.stdin = open("예제.txt", "r")
from itertools import combinations

n, m = map(int, input().split())
arr = [str(i+1) for i in range(n)]


for i in list(combinations(arr, m)):
    print(" ".join(i))