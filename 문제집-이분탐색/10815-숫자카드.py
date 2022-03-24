import sys
sys.stdin = open("예제.txt", "r")

n = int(input())
card = list(map(int, input().split()))
card.sort()
m = int(input())
find_array = list(map(int, input().split()))
answer = []

def binary_search(arr, x):
    start = 0
    end = len(arr)-1

    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == x:
            return 1
        elif arr[mid] < x:
            start = mid + 1
        elif arr[mid] > x:
            end = mid - 1
    return 0

for i in find_array:
    answer.append(binary_search(card, i))

print(*answer)