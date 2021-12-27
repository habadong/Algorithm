import sys
sys.stdin = open("예제.txt", "r")

## Bad Code ##
# for i in range(int(input())):
#     inputStr = input()
#     arr = list(inputStr)
#     MAP.append(arr)

MAP = [list(map(int, input().split())) for _ in range(int(input()))]

print(MAP)