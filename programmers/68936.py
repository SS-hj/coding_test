def solution(arr):
    ans = [0,0]
    def quad(r,c,k):
        tg = arr[r][c]
        for i in range(k):
            for j in range(k):
                if arr[r+i][c+j] != tg:
                    quad(r, c, k//2)
                    quad(r, c+k//2, k//2)
                    quad(r+k//2, c, k//2)
                    quad(r+k//2, c+k//2, k//2)
                    return
        ans[tg] += 1
    quad(0,0,len(arr))
    return ans