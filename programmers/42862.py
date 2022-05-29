def solution(n, lost, reserve):
    student = [1]*(n+1)
    for i in lost:
        student[i] = 0
    for i in reserve:
        student[i] += 1
    for s in range(1,len(student)-1):
        if student[s] == 0:
            if student[s-1] > 1:
                student[s] += 1
                student[s-1] -= 1
            elif student[s+1] > 1:
                student[s] += 1
                student[s+1] -= 1
    answer = -1 # student가 [1]*(n+1) 였으므로
    for s in student:
        if s >= 1:
            answer += 1
    return answer