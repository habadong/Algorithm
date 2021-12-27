import sys
sys.stdin = open("예제.txt", "r")

number = []
for i in range(9):
    number.append(int(input()))

print(max(number))
print(number.index(max(number))+1)
