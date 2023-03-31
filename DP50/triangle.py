class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        for i in range(1, len(triangle)):
            for j in range(i+1):
                triangle[i][j] += min(triangle[i-1][j-(j>0)],triangle[i-1][j-(j==i)])
        return min(triangle[-1])