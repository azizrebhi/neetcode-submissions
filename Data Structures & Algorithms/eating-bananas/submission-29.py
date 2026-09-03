import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r=1,max(piles)
        res=0
        while l<=r : 
            total_time=0
            m=(r+l)//2
            for p in piles : 
                total_time+=math.ceil(p/m)
            if total_time>h:
                l=m+1
            else :
                res=m
                r=m-1
        return res
        
            