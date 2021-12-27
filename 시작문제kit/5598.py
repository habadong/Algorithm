import sys
sys.stdin = open("예제.txt", "r")

a = list(input())
answer = ''
for i in a:
    if (ord(i)-3) < 65:
        answer += chr(ord(i)+23)
    else:
        answer += chr(ord(i)-3)
print(answer)