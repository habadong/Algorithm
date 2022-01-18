# 3
# 1001101 10010
# 1001001 11001
# 1000111 1010110
# 이진수 쌍의 합을 구하라
import sys
sys.stdin = open("예제.txt", "r")

for _ in range(int(input())):
    A, B = map(int, input().split())
    print(bin(A) + bin(B))