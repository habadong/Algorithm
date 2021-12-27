import sys
sys.stdin = open("예제.txt", "r")

from functools import reduce

n = int(input())
score = list(map(int, input().split(' ')))
m = max(score)
aver = reduce(lambda a, b: a+b, list(map(lambda a: a/m*100, score)), 0) / n

print(aver)