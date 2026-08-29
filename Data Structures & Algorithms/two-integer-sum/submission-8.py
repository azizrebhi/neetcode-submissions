class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m={}
        for i ,c in enumerate(nums):
            m[c]=i
        for i in range(len(nums)):
            new_target=target-nums[i]
            if new_target in m and m[new_target]!=i :
                return [i,m[new_target]]
        return False