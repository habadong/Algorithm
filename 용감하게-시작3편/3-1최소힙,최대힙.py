# 최소힙
import heapq
heap = []
heapq.heappush(heap, 3)
heapq.heappush(heap, 1)
heapq.heappush(heap, 10)
heapq.heappush(heap, 5)
heapq.heappush(heap, 8)

#      1 <--- Root 
#    /   \ 
#   3     5 
#  / \   / 
# 4   8 7

# 힙의 길이
print(len(heap))
# 5

# 힙의 루트 원소 제거
heapq.heappop(heap)


# 최대힙 구현
import sys, heapq  
heap = []  
 
for i in range(int(sys.stdin.readline())):  
    N = int(sys.stdin.readline()) * -1  
  if N == 0:  
        if len(heap) == 0:  
            print(0)  
        else:  
            print(heapq.heappop(heap) * -1)  
    else:  
        heapq.heappush(heap, N)

# -1을 곱해서 최대힙을 구현하였다