class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        for i in range(len(grid)):
          for j in range(len(grid[0])):
            if grid[i][j]==-1 or grid[i][j]==0:
                continue 
            visit=set()
            queue=deque()
            queue.append((i,j))
            visit.add((i,j))
            length=0
            F=False
            while queue :
                for k in range(len(queue)):
                    r,c=queue.popleft();
                    if grid[r][c]==0:
                        grid[i][j]=length
                        F=True
                    neighbors=[[0,1],[0,-1],[1,0],[-1,0]]
                    for dr,dc in neighbors : 
                      NR,NC=r+dr,c+dc
                      if (min(NR,NC)<0  or NR==len(grid) or (NR,NC) in visit  
                         or NC==len(grid[0]) or grid[NR][NC]==-1 ) :
                          continue 
                      queue.append((NR,NC))
                      visit.add((NR,NC))
                length+=1
                if F : 
                    break 
                    




