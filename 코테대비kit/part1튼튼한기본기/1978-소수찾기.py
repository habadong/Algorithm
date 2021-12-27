import sys
sys.stdin = open("예제.txt", "r")

n = int(input())
arr = list(map(int, input().split()))
answer = 0

def func(a):
    if a == 1:
        return False
    elif a == 2:
        return True
    for i in range(2, a):
        if a % i == 0:
            return False
    return True

for i in arr:
    if func(i):
        answer += 1

print(answer)