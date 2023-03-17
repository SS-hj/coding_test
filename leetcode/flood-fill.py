from collections import deque
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        n, m = len(image), len(image[0])
        dr = [-1,1,0,0]
        dc = [0,0,-1,1]
        q = deque([(sr,sc)])
        check = image[sr][sc]
        while q:
            r, c = q.popleft()
            image[r][c] = color
            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i]
                if 0<=nr<n and 0<=nc<m and image[nr][nc]!= color and image[nr][nc]==check:
                    q.append((nr,nc))
        return image