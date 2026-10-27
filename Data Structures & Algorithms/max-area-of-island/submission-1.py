class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        ROWS,COLS=len(grid),len(grid[0])
        maxSize=0
        def dfs(r,c):
            if min(r,c)<0  or r==ROWS or c==COLS or grid[r][c]==0:
                return 0
            grid[r][c]=0
            curSize=1
            for dr, dc in directions:
                curSize+=dfs(r+dr,c+dc)
            return curSize

        for r in range(ROWS) :
           for c in range(COLS) :
              if grid[r][c]==1:
                curSize=dfs(r,c)
                maxSize=max(maxSize,curSize)
        return maxSize

