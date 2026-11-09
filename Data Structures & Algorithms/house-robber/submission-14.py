class Solution:
    def rob(self, nums: List[int]) -> int:
        def helper(n,cache):
            if n==0 :
                return nums[n]
            if n==1:
                return max(nums[n],nums[n-1])
            if n  in cache :
                return cache[n]
            cache[n]=max(helper(n-2,cache)+nums[n],helper(n-1,cache))
            return cache[n]
            
        return helper(len(nums)-1,{})

            