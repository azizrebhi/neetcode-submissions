class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top ,bot=0 ,len(matrix)-1
        while top<=bot : 
            m=(top+bot)//2
            if  matrix[m][0]<=target and matrix[m][len(matrix[0])-1]>=target :
                right ,left = 0,len(matrix[0])-1
                while right<=left : 
                    m1=(right+left)//2 
                    if matrix[m][m1]>target : 
                        left=m1-1
                    elif matrix[m][m1]<target :
                        right =m1+1
                    else:
                         return True
                return False
            elif matrix[m][0]>target :
                bot=m-1
            else  :
                top=m+1
        return False