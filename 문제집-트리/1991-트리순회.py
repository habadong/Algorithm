import sys
sys.stdin = open("예제.txt", "r")

n = int(input())
tree = [list(map(str, input().split())) for i in range(n)]
answer = [[],[],[]]
tree.sort(key=lambda x:x[0])

def preorder(x):
    index = ord(x) - 65
    if index >= 0:
        answer[0].append(tree[index][0])
        preorder(tree[index][1])
        preorder(tree[index][2])

def inorder(x):
    index = ord(x) - 65
    if index >= 0:
        inorder(tree[index][1])
        answer[1].append(tree[index][0])
        inorder(tree[index][2])


def postorder(x):
    index = ord(x) - 65
    if index >= 0:
        postorder(tree[index][1])
        postorder(tree[index][2])
        answer[2].append(tree[index][0])


preorder('A')
inorder('A')
postorder('A')
for i in answer:
    print("".join(i))