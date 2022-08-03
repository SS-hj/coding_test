def solution(n):
    queen = [0]*n # 1차원 row 배열에 col값을 넣는 배열 (각 row에 각기 다른 col만 가능)
    def dfs(row):
        count = 0
        if n == row: #마지막 row까지 퀸을 놓았으면 count+=1
            return 1
        for col in range(n):
            queen[row] = col # 퀸을 (row, col)에 놓음
            for x in range(row):
                if queen[x] == queen[row]: #동일한 열에 놓은 퀸이 있는지 확인
                    break
                if abs(queen[x]-queen[row]) == (row-x): #열들의 차 == 행들의 차 ~> 대각선에 놓인 퀸
                    break
            else: # 제외당하지 않은 경우 / 조건들에 통과된 퀸 summation
                count += dfs(row+1)
        return count
    return dfs(0)