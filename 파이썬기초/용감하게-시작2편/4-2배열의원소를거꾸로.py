# arr.reverse()
import sys
sys.stdin = open("예제.txt", "r")

A = int(input())
B = int(input())

arr_B = [int(i) for i in str(B)]
arr_B.reverse()
print(arr_B)

for i in range(len(arr_B)):
    print(A * arr_B[i])
print(A * B)