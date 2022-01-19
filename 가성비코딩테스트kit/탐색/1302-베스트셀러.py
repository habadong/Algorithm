import sys
sys.stdin = open("예제.txt", "r")

n = int(input())
arr = {}
answer = []
for i in range(n):
    book = input()
    if book in arr:
        arr[book] += 1
    else:
        arr[book] = 1

best = sorted(arr.items(), key=lambda x : x[1])

for i in best:
    if best[-1][1] == i[1]:
        answer.append(i[0])
        
answer.sort()
print(answer[0])