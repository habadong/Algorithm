import sys
sys.stdin = open("예제.txt", "r")

a = input()
b = input()
index = len(b)
for i in b:
    index = index - 1
    print(int(b[index]) * int(a))
print(int(a) * int(b))