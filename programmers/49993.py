def solution(skill, skill_trees):
    cnt = 0
    for user_skill in skill_trees:
        temp = []
        for s in skill:
            try:
                temp.append(list(user_skill).index(s))
            except:
                temp.append(27)
        if temp == sorted(temp):
            cnt += 1
    return cnt