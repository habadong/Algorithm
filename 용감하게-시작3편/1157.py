import sys
sys.stdin = open("예제.txt", "r")

from collections import Counter

alph = sys.stdin.readline().rstrip().upper()
m = Counter(alph).most_common()
val = Counter(alph).values()

if list(val).count(m[0][1]) > 1:
    print("?")
else:
    print(m[0][0])