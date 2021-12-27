from queue import PriorityQueue

que = PriorityQueue() # 우선순위 큐 생성

# put()을 이용하여 우선순위 큐에 값 삽입 append()가 아니니 주의

que.put(4)
que.put(10)
que.put(2)

for i in range(len(que.queue)):
    print(que.queue[i], end=" ")

# 우선순위 큐 값 제거
que.get()