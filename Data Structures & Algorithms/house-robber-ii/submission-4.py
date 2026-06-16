class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0
        if len(nums)==1:
            return nums[0]

        for i in range(len(nums)-1):
                temp = max(nums[i] + rob1, rob2)
                rob1 = rob2
                rob2 = temp
        rob1x, rob2x = 0, 0
        for j in range(1,len(nums)):
                temp = max(nums[j] + rob1x, rob2x)
                rob1x = rob2x
                rob2x = temp
        return max(rob2,rob2x)