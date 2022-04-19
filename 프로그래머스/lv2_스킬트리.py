def solution(skill, skill_trees):    
    answer = [0] * len(skill_trees)

    for i in range(len(skill_trees)):
        s = list(skill)
        for j in skill_trees[i]:
            if j in s:
                if s.index(j) == 0:
                    s.pop(0)
                elif s.index(j) != 0:
                    answer[i] = 1
    
    return len(skill_trees) - sum(answer)