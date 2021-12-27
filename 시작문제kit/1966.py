import sys
sys.stdin = open("예제.txt", "r")

t = int(input())

for i in range(t):
    n, question = map(int, input().split())
    prior = list(map(int ,sys.stdin.readline().rstrip().split()))
    array = [i for i in range(n)]
    done = []
    while prior:
        doc = prior.pop(0)
        if any(doc < v for v in prior):
            prior.append(doc)
            array.append(array.pop(0))
        else:
            done.append(array.pop(0))

    print(done.index(question)+1)