class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(0,len(matrix)):
            l,r=0,len(matrix[i])-1
            while l<=r :
                m=(r+l)//2
                if matrix[i][m]>target :
                    r=m-1
                elif matrix[i][m]<target :
                    l=m+1
                else :
                    return True 
        return False 



