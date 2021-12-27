import sys
sys.stdin = open("예제.txt", "r")

s = list(input())
a = [-1 for i in range(26)]
answer = ''
for v in s :
    a[ord(v)-97] = s.index(v) 
for v in a :
    answer += str(v) + " "

print(answer)