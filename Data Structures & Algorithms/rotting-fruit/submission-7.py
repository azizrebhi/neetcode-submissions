class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS=len(grid)
        COLS=len(grid[0])
        queue=deque()
        time=0
        def bfs(r,c) : 
          if  min(r,c)<0 or  r==ROWS or c ==COLS or grid[r][c]==0  :
            return
          queue.append((r,c))
          grid[r][c]=0
        for i in range(ROWS):
           for j in range(COLS):
              if grid[i][j]==2 : 
                 queue.append((i,j))
                 grid[i][j]=0
        while queue :
            for k in range(len(queue)):
              r,c=queue.popleft()
              bfs(r+1,c)
              bfs(r-1,c)
              bfs(r,c+1)
              bfs(r,c-1)
            if len(queue)>0 : 
                time+=1
           
        for i in range(ROWS):
           for j in range(COLS): 
            if grid[i][j]==1 : 
                return -1
        return time
        
        
        

        