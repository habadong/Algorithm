import sys
sys.stdin = open("예제.txt", "r")
from functools import reduce

odd = []
for i in range(7):
    a = int(input())
    if a % 2 == 1:
        odd.append(a)

if len(odd) == 0:
    print(-1)
else:
    print(reduce(lambda a, b: a+b, odd, 0))
    print(min(odd))