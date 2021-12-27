import sys
sys.stdin = open("예제.txt", "r")

h, w = map(int, input().split())
arr = list(map(int, input().split()))
answer = 0

for i in range(1, w-1):
    left_height = arr[i]
    right_height = arr[i]
    for l in range(0,i):
        if arr[l] > left_height:
            left_height = arr[l]
    for r in range(i, w):
        if arr[r] > right_height:
            right_height = arr[r]
    m = min(left_height, right_height)
    answer += m - arr[i]

print(answer)