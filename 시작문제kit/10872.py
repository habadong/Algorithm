import sys
sys.stdin = open("예제.txt", "r")

a = int(input())
answer = 1
def func(x):
    global answer
    if x == 0:
        return 1

    func(x-1)
    answer *= x
    return answer

print(func(a))