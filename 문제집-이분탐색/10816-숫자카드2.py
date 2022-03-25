import sys
sys.stdin = open("예제.txt", "r")

n = int(input())
card = list(map(int, input().split()))
m = int(input())
find_array = list(map(int, input().split()))
answer = []

card.sort()

def lower_bound(arr, x):
    start = 0
    end = len(arr)

    while start < end:
        mid = (start + end) // 2

        if arr[mid] >= x:
            end = mid
        else:
            start = mid + 1
    return end

def upper_bound(arr, x):
    start = 0
    end = len(arr)

    while start < end:
        mid = (start + end) // 2

        if arr[mid] > x:
            end = mid
        else:
            start = mid + 1
    return end

for i in find_array:
    answer.append(upper_bound(card,i) - lower_bound(card,i))

print(*answer)

