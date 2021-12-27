import sys
sys.stdin = open("예제.txt", "r")

a, b = map(int, input().split())
c = a if a > b else b
d = b if a > b else a
def g(x, y):
    return g(y, x%y) if y else x
def l(x, y):
    return int(x * y / g(x, y))
print(g(c,d))
print(l(c,d))