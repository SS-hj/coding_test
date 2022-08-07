def solution(line):
    points = set()
    maxX, maxY, minX, minY = -10e10, -10e10, 10e10, 10e10
    for i in range(len(line)):
        for j in range(i+1, len(line)):
            A, B, E = line[i]
            C, D, F = line[j]
            tmp = A * D - B * C
            if tmp != 0 and (B*F-E*D)%tmp == 0 and (E*C-A*F)%tmp == 0:
                X, Y = (B*F-E*D)//tmp, (E*C-A*F)//tmp # 교점 공식 적용
                maxX, maxY, minX, minY = max(maxX, X), max(maxY, Y), min(minX, X), min(minY, Y)
                points.add((X, Y))
    answer = [["." for c in range(maxX-minX+1)] for r in range(maxY-minY+1)]
    for x, y in points:
        answer[maxY-y][x-minX] = "*" # 인덱스 계산방식 주의
    return ["".join(row) for row in answer]