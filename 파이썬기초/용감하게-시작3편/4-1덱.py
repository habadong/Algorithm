# 덱 사용
from collections import deque

deq = deque() # 덱 초기화

deq = deque([i for i in range(1, 5)])

deq.appendleft(10)
# [10, 1, 2, 3, 4]

deq.append(-10)
# [10, 1, 2, 3, 4, -10]

# 오른쪽 값 제거
print(deq.pop())

# 왼쪽 값 제거
print(deq.popleft())

# 덱 길이
len(deq)

deq.rotate(-1) # 음수이면 왼쪽으로 회전
# [2, 3, 4, 1]
