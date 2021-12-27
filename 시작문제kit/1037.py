import sys
sys.stdin = open("예제.txt", "r")

n = input()
a = list(map(int,input().split(" ")))
a.sort()
if int(n) % 2 == 0:
    print(a[0] * a[int(n)-1])
elif int(n) % 2 != 0:
    print(a[int((int(n)-1)/2)] ** 2)