from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS , COLS=len(matrix),len(matrix[0])
        top,bot=0,ROWS-1
        while top<=bot :
            row=(bot+top)//2 
            if matrix[row][-1]<target :
                top=row+1
            elif target < matrix[row][0]:
                bot=row-1
            else: break
        if not(top<=bot ):
            return False 
        row=(bot+top)//2 
        s,k=0,COLS-1
        while s<=k :
            m=(s+k)//2
            if matrix[row][m]>target :
                k=m-1
            elif matrix[row][m]<target : 
                s=m+1
            else : 
                return True
        return False
                 

        