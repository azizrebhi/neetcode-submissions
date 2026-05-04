class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left , right = 0,len(heights)-1
        maxi=0
        while left<right :
            area=min(heights[left],heights[right])*(right-left)
            maxi=max(maxi,area)
            if (heights[left]<heights[right]) :
                left+=1
            else :
                right-=1
        return maxi