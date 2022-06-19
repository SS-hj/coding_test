def solution(rows, columns, queries):
    arr = []
    for r in range(rows):
        arr.append(list(range(1+r*columns,columns+1+r*columns)))
    answer = []
    for q in queries:
        x1,y1,x2,y2 = q[0],q[1],q[2],q[3]
        temp = []
        for y in range(y1-1,y2):
            temp.append(arr[x1-1][y])
        for x in range(x1,x2):
            temp.append(arr[x][y2-1])
        for y in range(y2-2,y1-2,-1):
            temp.append(arr[x2-1][y])
        for x in range(x2-2,x1-1,-1):
            temp.append(arr[x][y1-1])
        temp.insert(0,temp.pop())
        idx = 0
        for y in range(y1-1,y2):
            arr[x1-1][y] = temp[idx]
            idx += 1
        for x in range(x1,x2):
            arr[x][y2-1] = temp[idx]
            idx += 1
        for y in range(y2-2,y1-2,-1):
            arr[x2-1][y] = temp[idx]
            idx += 1
        for x in range(x2-2,x1-1,-1):
            arr[x][y1-1] = temp[idx]
            idx += 1
        answer.append(min(temp))
    return answer