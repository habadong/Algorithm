import sys
sys.stdin = open("예제.txt", "r")

t = int(input())

for v in range(t) :
    n = str(format(int(input()), "b"))[::-1]
    answer = ''
    for i, val in enumerate(n) :
        if val == '1' :
            answer += str(i) + ' '
    print(answer)