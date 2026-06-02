class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        queue=deque()
        ROW=len(grid)
        COL=len(grid[0])
        length=1
        visit=set()
        for i in range(ROW):
           for j in range(COL):
                if grid[i][j]==0 : 
                    queue.append((i,j))
        while queue :
            for k in range(len(queue)):
                    r,c=queue.popleft();
                    neighbors=[[0,1],[0,-1],[1,0],[-1,0]]
                    for dr,dc in neighbors : 
                      NR,NC=r+dr,c+dc
                      if (min(NR,NC)<0  or NR==len(grid) or (NR,NC) in visit  
                         or NC==len(grid[0]) or grid[NR][NC]==-1 or grid[NR][NC]==0)  :
                          continue
                      grid[NR][NC]=length 
                      queue.append((NR,NC))
                      visit.add((NR,NC))
            length+=1