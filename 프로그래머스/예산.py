## 첫 풀이 백트래킹을 활용해서 하려고 했는데 시간 초과가 나왔음 
def solution(d, budget):
    answer = []
    array = d
    array.sort()
    arr = []
    
    def dfs(x):
        if len(arr) > 0 and sum(arr) >= budget:
            if sum(arr) == budget:
                answer.append(len(arr))
            return
        for i in range(x, len(d)):
            arr.append(array[i])
            dfs(i+1)
            arr.pop()

    dfs(0)
    
    return max(answer)
