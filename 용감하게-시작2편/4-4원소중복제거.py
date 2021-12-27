# alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'a', 'b', 'c', 'd' ] 
# alpha = list(set(alpha))

lst = [[1,2], [1,2], [1]]
print(list(set(map(tuple, lst))))