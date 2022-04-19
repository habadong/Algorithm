import math
def solution(n, words):
    length = len(words)
    dic = []
    a = 0
    b = 0
    ## 중복하는지 & 알맞게 단어를 말했는지
    for i in range(length):
        if dic:  
            if words[i] in dic or dic[-1][-1] != words[i][0]:
                if (i+1) % n == 0:
                    a = n
                else:
                    a = (i+1) % n
                b = math.ceil((i+1) / n)
                break
        dic.append(words[i])
    return [a, b]