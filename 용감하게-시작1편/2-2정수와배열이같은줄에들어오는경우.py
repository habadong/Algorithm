import sys
sys.stdin = open("예제.txt", "r")

N, *arr = map(int, input().split()) ## 컨테이너 타입의 데이터를 unpacking 할때