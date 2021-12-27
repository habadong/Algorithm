import sys
sys.stdin = open("예제.txt", "r")

n = int(input())
array = list(map(int, input().split(' ')))

print(min(array), max(array))