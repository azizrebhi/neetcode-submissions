class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS,COLS=len(grid),len(grid[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        
        q=deque()
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c]==0:
                    q.append((r,c))          
        count=0
        visit=set()
        while len(q)>0:
                for i in range(len(q)):
                    r,c=q.popleft()
                    if grid[r][c]>0 : 
                        grid[r][c]=count
                    for dr,dc in directions:
                        NR,NC=r+dr,c+dc
                        if min(NR,NC)<0 or NR==ROWS or NC==COLS or grid[NR][NC]==-1 or (NR,NC) in  visit: 
                            continue
                        q.append((NR,NC))
                        visit.add((NR,NC))
                count+=1
            

        
        

        
                    