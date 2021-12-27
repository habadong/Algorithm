import sys
sys.stdin = open("예제.txt", "r")

# 바텀업 다이나믹 프로그래밍
n = int(input())
arr = [0, 1]
for i in range(19):
    arr.append(arr[i] + arr[i+1])
print(arr[n])

# 업다운 다이나믹 프로그래밍
# arr = [0] * 21
# def fibo(x):
#     if x == 0:
#         return 0
#     if x == 1 or x == 2:
#         return 1
#     if arr[x] != 0:
#         return arr[x]
#     arr[x] = fibo(x-1) + fibo(x-2)
#     return arr[x]

# print(fibo(n))