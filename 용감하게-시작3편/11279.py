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