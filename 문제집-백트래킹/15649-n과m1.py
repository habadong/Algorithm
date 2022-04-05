import sys
sys.stdin = open("예제.txt", "r")

n, m = map(int, input().split())

arr = [0] * m
isused = [0] * (n+1)

def func(k):
    # base condition
    if k == m:
        print(*arr)
        return
    
    for i in range(1, n+1):
        if isused[i] == 0:
            arr[k] = i # 해당 k자리에 사용하지 않은 숫자 i 를 넣는다
            isused[i] = 1 # 그 숫자 썻다고 1로 표시 
            func(k+1) # 재귀적으로 k+1 하여 다음 자리수로 넘긴다
            isused[i] = 0 # 숫자 i를 0으로 표시하는 것은 k+1번째 자리(다음자리)에서 사용할 숫자는 모두 사용 했기 때문에 다시 사용할수 있게 표시한다

func(0)