# for 문 2개를 사용해서 nC2를 구하는 방법은 다음과 같음

for i in range(0, N-1):
    for j in range(i+1, N):
        print(i, j)