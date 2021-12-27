import sys
sys.stdin = open("예제.txt", "r")
import heapq

n = int(input())
heap = []

for i in range(n):
    x = int(sys.stdin.readline().rstrip())
    if x:
        heapq.heappush(heap, (-x, x))
    else:
        if heap:
            print(heap[0][1])
            heapq.heappop(heap)
        else:
            print(0)