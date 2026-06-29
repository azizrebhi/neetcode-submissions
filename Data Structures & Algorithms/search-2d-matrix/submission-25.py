class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r,l=0,len(matrix)-1
        while r<=l : 
            m=(r+l)//2
            if matrix[m][0]<=target and matrix[m][len(matrix[0])-1]>=target :
               r1,l1=0,len(matrix[0])-1
               while r1<=l1 :
                  m1=(r1+l1)//2 
                  if matrix[m][m1]>target :
                    l1=m1-1
                  elif matrix[m][m1]<target : 
                      r1=m1+1
                  else :
                      return True
               return False 
            elif matrix[m][0]>target : 
                l=m-1
            else :
                r=m+1
        return False 
            
                
                
