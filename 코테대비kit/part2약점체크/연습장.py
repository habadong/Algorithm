import sys
sys.stdin = open("예제.txt", "r")

def quick_sort(arr, start, end):
    # 원소가 1개인 경우 종료
    if start >= end: 
        return

    # 피벗은 첫 번째 원소
    pivot = start
    left = start + 1
    right = end

    while(left <= right):
        # 피벗보다 큰 데이터를 찾을 때까지 반복
        while(left <= end and arr[left] <= arr[pivot]):
            left += 1
        # 피벗보다 작은 데이터를 찾을 때까지 반복
        while(right > start and arr[right] >= arr[pivot]):
            right -= 1
        if left > right: # 엇갈렸다면, 작은 데이터(right)와 피벗을 교체
            arr[right], arr[pivot] = arr[pivot], arr[right]
        else: # 엇갈리지 않았다면, 작은 데이터와 큰 데이터를 교체
            arr[left], arr[right] = arr[right], arr[left]
    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행
    quick_sort(arr, start, right - 1)
    quick_sort(arr, right + 1, end)

array = [5,6,2,5,7,3,1,9]
quick_sort(array, 0, len(array)-1)

def ez_quick(arr):
    # 리스가 하나 이하의 원소만을 담고 있다면 종료
    if len(arr) <= 1:
        return arr
    pivot = arr[0] # 피벗은 첫 번째 원소
    tail = arr[1:] # 피벗을 제외한 리스트

    left_side = [x for x in tail if x <= pivot] # 분할된 왼쪽 부분
    right_side = [x for x in tail if x > pivot] # 분할된 오른쪽 부분

    # 분할 이후 왼쪽과 오른쪽 부분에서 각각 정렬을 수행하고, 피벗과 결합하여 전체 리스트를 반환
    return ez_quick(left_side) + [pivot] + ez_quick(right_side)

print(ez_quick(array))

