class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        ROW,COL=len(grid),len(grid[0])
        if grid[0][0]==1 or grid[ROW-1][COL-1]: 
            return -1
        if ROW == 1 and COL == 1:
            return 1
        visit=set()
        queue=deque()
        queue.append((0,0))
        visit.add((0,0))
        length=1
        while queue:
            for i in range(len(queue)):
                r,c=queue.popleft()
                if r==ROW-1 and c==COL-1 :
                    return length
                neighbors = [[0, 1], [0, -1], [1, 0], [-1, 0],[1,1], [1,-1], [-1,1], [-1,-1]]
                for dr, dc in neighbors:
                    newRow=r+dr 
                    newCol=c+dc
                    if (min(newRow,newCol)<0 or (newRow ,newCol) in visit or 
                     newRow==ROW or newCol==COL or grid[newRow][newCol]==1 ) : 
                       continue
                    queue.append((newRow,newCol))
                    visit.add((newRow,newCol))
            length += 1
        return -1




               