class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS,COLS=len(grid),len(grid[0])
        queue=deque()
        visit=set()
        directions=[[1,0],[-1,0],[0,1],[0,-1]]
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c]==2:
                    queue.append((r,c))
                    visit.add((r,c))
        time=0
        while len(queue)>0:
            for i in range(len(queue)):
               r,c=queue.popleft()
               for dr,dc in directions:
                 NEWR=r+dr
                 NEWC=c+dc
                 if min(NEWR,NEWC)<0 or NEWR==ROWS or NEWC==COLS or (NEWR,NEWC) in visit or grid[NEWR][NEWC]==0 : 
                    continue 
                 if grid[NEWR][NEWC]==1:
                    grid[NEWR][NEWC]=2
                 queue.append((NEWR,NEWC))
                 visit.add((NEWR,NEWC))
            if len(queue) > 0:
                time += 1
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c]==1:
                    return -1
        return time

        
        