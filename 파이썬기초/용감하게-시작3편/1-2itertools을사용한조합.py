# 파이썬에서 조합을 구하는 방법은 아래와 같음

from itertools import combinations
print(list(combinations([1,2,3,4], 3)))

# combinations 의 첫 번째 인자에 배열을 넣고, 두 번째 인자에는 nCm 이라면 m을 넣는다

# [(1, 2, 3), (1, 2, 4), (1, 3, 4), (2, 3, 4)]