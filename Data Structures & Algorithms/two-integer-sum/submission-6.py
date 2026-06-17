class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
       S={}
       for i ,num in enumerate(nums):
           S[target-num]=i
       for j in range(len(nums)):
            if nums[j] in S and j!=S[nums[j]]:
                return [j,S[nums[j]]]