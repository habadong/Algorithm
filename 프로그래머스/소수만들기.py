from itertools import combinations
import math
def solution(nums):
    answer = 0
    array = combinations(nums, 3)
    for i in array:
        if is_prime(sum(i)):
            answer += 1

    return answer

def is_prime(x):
    if x == 1:
        return False
    if x == 2:
        return True
    if x % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(x))+1):
        if x % i == 0:    
            return False
    return True