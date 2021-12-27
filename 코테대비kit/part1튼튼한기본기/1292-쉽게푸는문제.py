import sys
sys.stdin = open("예제.txt", "r")

a, b = map(int, input().split())
arr = []
for i in range(1001):
    for j in range(i):
        arr.append(i)
print(sum(arr[a-1:b]))

# 다른사람 풀이
# a b 의 범위가 1000까지 였기 때문에 반복문 범위는 46까지만 구해도 된다
arr1 = [0]
for i in range(46):
    for j in range(i):
        arr1.append(i)