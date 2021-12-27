import sys
sys.stdin = open("예제.txt", "r")

t = int(input())

for i in range(t):
    ps = list(sys.stdin.readline().rstrip())
    length = len(ps)
    left = 0
    right = 0
    answer = "YES"
    if length % 2 == 1:
        answer = "NO"
    else:
        for i in range(length):
            pop = ps.pop(0)
            if pop == '(':
                if left >= length / 2:
                    answer = "NO"
                    break
                left += 1
            elif pop == ')':
                if left == 0:
                    answer = "NO"
                    break
                elif left == right:
                    answer = "NO"
                    break
                right += 1
    print(answer)