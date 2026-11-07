class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l,r=0,len(heights)-1
        res=min(heights[r],heights[l])*(r-l)
        while l<r:
            if heights[l]>heights[r]: 
                r-=1
                if res<min(heights[r],heights[l])*(r-l):
                    res=min(heights[r],heights[l])*(r-l)
                
                
            else :
                l+=1
                if res<min(heights[r],heights[l])*(r-l):
                    res=min(heights[r],heights[l])*(r-l)
                
                
        return res

                


            
