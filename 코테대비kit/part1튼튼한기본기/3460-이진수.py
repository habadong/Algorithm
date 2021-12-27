import sys
sys.stdin = open("예제.txt", "r")

t = int(input())

for i in range(t):
    answer = []
    n = list(format(int(input()), 'b'))
    n.reverse()
    
    for i in range(len(n)):
        if n[i] == "1":
            answer.append(i)
    print(*answer)    