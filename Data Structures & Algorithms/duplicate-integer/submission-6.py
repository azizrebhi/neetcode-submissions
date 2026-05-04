class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        S=set(nums)
        return not  len(S)==len(nums)