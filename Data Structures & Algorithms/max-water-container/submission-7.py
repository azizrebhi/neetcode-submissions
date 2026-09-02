class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maximum=0
        l,r=0,len(heights)-1
        while l<r : 
            storage=(r-l)*min(heights[r],heights[l])
            maximum=max(storage,maximum)
            if heights[r]>heights[l]:
                l=l+1
            else :
                r=r-1
        return maximum
