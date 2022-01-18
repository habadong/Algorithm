# ans = ???
# for num in arr:
#     if ans > num:
#         ans = num
# print(ans)

# 최대, 최소 범위를 정하기 애매한 상황에서 우아한 방법은 아래와 같다

import sys
ans = sys.maxsize

print(ans)

# 아무리 큰 정수라도 범위의 제한 없이 연산이 가능함. 따라서 ans에 ans += 1 연산이 가능하다
