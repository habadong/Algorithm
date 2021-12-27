import sys
sys.stdin = open("예제.txt", "r")

n, k = map(int, input().split())
coin = [int(input()) for _ in range(n)]
coin_list = [100001 for i in range(k+1)]
coin_list[0] = 0

for i in coin:
    for j in range(i, k+1):
        if j - i >= 0:
            coin_list[j] = min(coin_list[j-i] + 1, coin_list[j])
if coin_list[-1] == 100001:
    print(-1)
else:
    print(coin_list[-1])