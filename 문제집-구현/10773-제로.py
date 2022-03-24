import sys
sys.stdin = open("예제.txt", "r")

k = int(input())

array = []

for i in range(k):
    number = int(input())
    if number:
        array.append(number)
    else:
        array.pop()

print(sum(array))