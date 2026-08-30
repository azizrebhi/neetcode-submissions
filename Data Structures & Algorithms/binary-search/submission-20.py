class Solution:
    def search(self, nums: List[int], target: int) -> int:
        right,left=0,len(nums)-1
        while right<=left : 
            m=(right+left)//2
            if nums[m]>target:
                left=m-1
            elif nums[m]<target : 
                right=m+1
            else : 
                return m
        return -1