class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1

        ROWS,COLS=len(grid),len(grid[0])
        directions=[[0,1],[0,-1],[1,0],[-1,0],[1,1],[-1,-1]]
        queue=deque()
        queue.append((0,0))
        visit=set()
        visit.add((0,0))
        length=1
        while len(queue)>0:
            for i in range(len(queue)):
               r,c=queue.popleft()
               if r==ROWS-1 and c==COLS-1:
                   return length
               for dr,dc in directions : 
                 NEWR=r+dr
                 NEWC=c+dc
                 if min(NEWC,NEWR)<0 or NEWC==COLS or NEWR==ROWS or grid[NEWR][NEWC]==1 or (NEWR,NEWC) in visit :
                     continue
                 queue.append((NEWR,NEWC))
                 visit.add((NEWR,NEWC))
            length+=1
        return -1 
        
                 

