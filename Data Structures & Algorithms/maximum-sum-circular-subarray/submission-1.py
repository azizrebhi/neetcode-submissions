class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        maxSum=nums[0]
        minSum=nums[0]
        curSum=0
        curMin = 0
        total=0
        for n in nums: 
            total+=n
            curSum=n+max(0,curSum)
            curMin=n+min(0,curMin)
            minSum=min(minSum,curMin)
            maxSum=max(maxSum,curSum)
        if maxSum < 0:
           return maxSum

        return max(maxSum,total-minSum)