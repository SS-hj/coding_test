class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        n = len(dungeon)
        m = len(dungeon[0])
        for r in range(n-1,-1,-1):
            for c in range(m-1,-1,-1):
                if r==n-1 and c==m-1:
                    dungeon[r][c] = max(1, 1-dungeon[r][c])
                elif r==n-1:
                    dungeon[r][c] = max(1,dungeon[r][c+1]-dungeon[r][c])
                elif c==m-1:
                    dungeon[r][c] = max(1,dungeon[r+1][c]-dungeon[r][c])
                else:
                    dungeon[r][c] = max(1,min(dungeon[r+1][c]-dungeon[r][c],dungeon[r][c+1]-dungeon[r][c]))
        return dungeon[0][0]