import sys
sys.stdin = open("예제.txt", "r")

a, b = map(int, input().split())

if a < b:
    print('<')
elif b < a:
    print('>')
else :
    print('==')