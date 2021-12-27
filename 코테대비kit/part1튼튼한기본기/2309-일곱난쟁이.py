import sys
sys.stdin = open("예제.txt", "r")
from itertools import combinations

arr = [int(input()) for _ in range(9)]
a = combinations(arr, 7)
answer = []

for i in a:
    if sum(i) == 100:
        answer = list(i)
        answer.sort()
        break

for i in answer:
    print(i)