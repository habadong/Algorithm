import sys
sys.stdin = open("예제.txt", "r")

## 성공 O(N)
## 일차적으로 생각했을때 쉬운문제라 생각했지만 시간제한이 있는 문제였기 때문에
## 시간 복잡도를 생각해야했다. 이제는 코드 작성시 시간복잡도를 생각해야겠다.
## 연산속도를 줄이기위한 방법인 DP가 있는거 처럼, 연산속도를 줄이기 위해
## 연산과정에서 건물에 대한 정보를 저장(stack에 push)한것 처럼 보인다.
n = int(input())
tower = list(map(int, sys.stdin.readline().split()))
stack = []
answer = [0 for _ in range(n)]

for i in range(n):
    while stack:
        if tower[i] < stack[-1][1]:
            answer[i] = stack[-1][0] + 1
            break
        else:
            stack.pop()
    stack.append([i, tower[i]])
print(*answer)

### 실패 O(N^2)
'''
while stack:
    top = stack.pop()
    for i in range(len(stack)-1, -1, -1):
        if top <= stack[i]:
            answer.append(i+1)
            break
        elif i == 0 and top > stack[i]:
            answer.append(0)
    if len(stack) == 0:
        answer.append(0)
answer.reverse()
print(*answer)
'''