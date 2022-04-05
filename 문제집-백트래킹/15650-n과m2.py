import sys
sys.stdin = open("예제.txt", "r")

n, m = map(int, input().split())

array = []

def func(k):
    if len(array) == m:
        print(*array)
        return

    for i in range(k, n+1):
        # if i not in array:  # <--- 이부분은 중복체크를 하는부분으로 func(i+1)부터 한다면 굳이 필요하지 않은 부분이다
        array.append(i)
        func(i+1)
        array.pop()
func(1)

