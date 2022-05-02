from collections import deque

def solution(begin, target, words):
    answer = 0
    visited = [0] * len(words)
    queue = deque()
    queue.append((begin, 0))

    def func(x, v):
        alpCount = 0
        for i in range(len(v)):
            if v[i] == words[x][i]:
                alpCount += 1
        if alpCount == len(v) - 1:
            return True
        return False

    while queue:
        word, c = queue.popleft()

        if word == target:
            answer = c
            break

        for i in range(len(words)):
            if visited[i] == 0:
                if func(i, word):
                    queue.append((words[i], c+1))
                    visited[i] = 1

    return answer