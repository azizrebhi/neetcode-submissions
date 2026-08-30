class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS,COLS=len(matrix),len(matrix[0])
        left,right=0,ROWS*COLS-1
        while left<=right : 
            m=(left+right)//2
            r=m//COLS
            c=m%COLS
            if matrix[r][c]>target :
                right=m-1
            elif matrix[r][c]<target : 
                left=m+1
            else : 
                return True
        return False
