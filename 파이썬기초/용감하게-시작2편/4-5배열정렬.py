arr.sort() # 오름차순으로 정렬

arr.sort(reverse=True) # 내림차순으로 정렬

arr.sort(key=lambda x:(x[0], x[1])) # 람다식으로 원소가 리스트인 형태를 정렬

arr.sort(key=lambda x:(-x[1], x[2], -x[3], x[0])) # 람다식으로 내림차순 정렬

