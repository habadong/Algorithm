import sys
sys.stdin = open("예제.txt", "r")

s = list(input())
stack = []
stack.append(s.pop())

print(stack[len(stack)-1])

def func(length, arr):
    global stack
    top = len(stack)-1
    if length % 2 == 1:
        return 0

    if arr[0] == '(' or arr[0] == '[':
        stack.append(arr.pop(0))
        func(length-1, arr)
    elif arr[0] == ')':
        if stack[top] == '(':
            stack.pop()
            return func(length-1, arr) ## 2
    elif arr[0] == ']':
        if stack[top] == '['
            stack.pop()
            return func(length-1, arr) ## 3