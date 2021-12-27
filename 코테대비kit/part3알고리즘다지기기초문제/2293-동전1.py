import sys
sys.stdin = open("예제.txt", "r")

n, k = map(int, input().split())

coin = [int(input()) for _ in range(n)]

coin_list = [0 for _ in range(k+1)]

coin_list[0] = 1

for i in coin:
    for j in range(i, k+1):
        coin_list[j] += coin_list[j-i]

print(coin_list[k])