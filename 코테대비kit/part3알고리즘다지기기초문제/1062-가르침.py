import sys
sys.stdin = open("예제.txt", "r")
from itertools import combinations

n, k = map(int, input().split())
dic = {'b':20,'d':19,'e':18,'f':17,'g':16,'h':15,'j':14,'k':13,'l':12,'m':11,
    'o':10,'p':9,'q':8,'r':7,'s':6,'u':5,'v':4,'w':3,'x':2,'y':1,'z':0}

words = [set(sys.stdin.readline().rstrip()[4:-4]).difference('a', 'c', 'i', 'n', 't') for _ in range(n)]

def word_to_bin(word):
    bin = 0b0
    for i in word:
        bin = bin | (1 << dic[i])
    return bin

if k < 5:
    print(0)
else:
    bin_list = [word_to_bin(i) for i in words]
    sqard = [2 ** i for i in range(21)]
    MAX = 0
    
    for i in combinations(sqard, k-5):
        cur = sum(i)
        count = 0
        for num in bin_list:
            if num & cur == num:
                count += 1

        MAX = max(count, MAX)

    print(MAX)

