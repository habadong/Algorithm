import sys
sys.stdin = open("예제.txt", "r")

n, x = input().split()
num = input().split()
answer = ''
for a in num:
    if int(a) < int(x):
        answer += a + ' '
print(answer)