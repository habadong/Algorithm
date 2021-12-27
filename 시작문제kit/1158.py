import sys
sys.stdin = open("예제.txt", "r")

n, k = map(int, input().split())

circle = [i+1 for i in range(n)]
answer = []
index = 0

for i in range(n):
    index += k-1
    if index >= len(circle):
        index = index % len(circle)
    
    answer.append(str(circle.pop(index)))

print("<",", ".join(answer),">", sep='')
