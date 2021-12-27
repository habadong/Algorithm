import sys
sys.stdin = open("예제.txt", "r")

n = int(input())
num_arr = list(map(int, input().split()))
acc_arr = list(map(int, input().split()))

MAX = -100000001
MIN = 100000001

def func(count, result, pl, mi, mu, di):
    global MAX, MIN
    if count == n:
        MAX = max(result, MAX)
        MIN = min(result, MIN)
        return

    if pl:
        func(count+1, result + num_arr[count], pl-1, mi, mu, di)
    if mi:
        func(count+1, result - num_arr[count], pl, mi-1, mu, di)
    if mu:
        func(count+1, result * num_arr[count], pl, mi, mu-1, di)
    if di:
        func(count+1, int(result / num_arr[count]), pl, mi, mu, di-1)

func(1, num_arr[0], acc_arr[0], acc_arr[1], acc_arr[2], acc_arr[3])

print(MAX)
print(MIN)