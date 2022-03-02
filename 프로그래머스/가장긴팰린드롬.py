def solution(s):
    answer = 1
    length = len(s)
    for i in range(length-1, 0, -1):
        for j in range(0, i, 1):
            isPalindrome = True
            new_str = s[j:i+1]
            half = int(len(new_str) / 2)
            if answer > len(new_str):
                continue
            for a in range(half):
                start = a
                end = len(new_str) - a - 1
                if new_str[start] != new_str[end]:
                    isPalindrome = False
                    break
            if isPalindrome == True:
                answer = max(len(new_str), answer)

    return answer