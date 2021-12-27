import sys
sys.stdin = open("예제.txt", "r")

answer = 0
num = 0
for _ in range(10):
    o, i = map(int, input().split())
    num -= o
    num += i
    if num > answer:
        answer = num

print(answer)