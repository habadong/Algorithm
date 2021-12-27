import sys
sys.stdin = open("예제.txt", "r")

n, k = map(int, input().split())
arr = list(map(int, input().split()))
plug = arr[:n]
sche = arr[n:k]
answer = 0

for i in range(len(sche)):
    if sche[i] not in plug:

        plug_list = {}
        for j in plug:
            plug_list[j] = 0

        for k in range(i+1, len(sche)):
            if plug_list.get(sche[k]) != None:
                plug_list[sche[k]] += 1
        MIN = min(plug_list, key=plug_list.get)
        print(plug)
        plug.pop(plug.index(MIN))
        plug.append(sche[i])
        answer += 1

print(answer)


# 가장 나중에 사용되는 플러그를 뽑는다는 의미?